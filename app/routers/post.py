from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import and_
from starlette.status import HTTP_404_NOT_FOUND
from app.services.auth.user_data import get_user
from app.db.models import Post
from app.db import schemas
from app.services.db.sqlalchemy import service_session

router = APIRouter()


@router.get('/posts', response_model=list[schemas.PostList])
async def get_posts() -> list[schemas.PostList]:
    with service_session() as session:
        post_obj = session.query(Post).filter().all()
        return [schemas.PostList(**post_obj.__dict__) for post_obj in post_obj]


@router.post('/post/', response_model=schemas.PostDetail)
async def add_post(data: schemas.CreatePostModel,
                   user: Depends = get_user()) -> schemas.PostDetail:
    with service_session() as session:
        post_obj = Post(
            text=data.text,
            date_edited=datetime.utcnow(),
            user_id=user.id
        )
        session.add(post_obj)
        session.commit()
        session.refresh(post_obj)

        return schemas.PostDetail(**post_obj.__dict__)


@router.get('/posts/{post_id}', response_model=schemas.PostDetail)
async def get_post(post_id: str,
                   param: schemas.PostId = Depends()) -> schemas.PostDetail:
    with service_session() as session:
        post_obj = session.query(Post).filter(Post.id == post_id).first()
        return schemas.PostDetail(**post_obj.__dict__)


@router.put('/post/{post_id}', response_model=schemas.PostDetail)
async def update_post(post_id: int, data: schemas.PostUpdate,
                      user: Depends = get_user()) -> schemas.PostDetail:
    with service_session() as session:
        post_obj = session.query(Post).filter(
            and_(Post.id == post_id, Post.user_id == user.id))
        if not post_obj:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)

        post_obj.update({**data.dict()})
        session.commit()
        post_obj = session.query(Post).filter(Post.id == post_id).first()

        return schemas.PostDetail(**post_obj.__dict__)


@router.delete('/post/{post_id}')
async def delete_post(post_id, user: Depends = get_user()):
    with service_session() as session:
        post_obj = session.query(Post).filter(
            and_(Post.id == post_id, Post.user_id == user.id)).first()
        if not post_obj:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)

        session.delete(post_obj)
        session.commit()


@router.post('/like/{post_id}')
async def like_post(post_id):
    pass
