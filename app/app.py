from fastapi import FastAPI

from app.config.settings import APP_NAME, API_VERSION
from app.routers import auth, post


app = FastAPI(title=APP_NAME, version=API_VERSION, redoc_url='',
              docs_url='/docs')

app.include_router(auth.router, tags=["Users"], prefix='/api/v1')
app.include_router(post.router, tags=["Posts"], prefix='/api/v1')

