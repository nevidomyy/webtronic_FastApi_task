# FastAPI Posts APP Task

#### Software development stack ####
Fastapi - web framework для API\
SQLAlchemy - ORM для работы с БД\
Alembic - Управление миграциями\
Pydantic - Валидация данных, с использованием @validator.




#### Build and run ####
1. Install **docker**: https://docs.docker.com/engine/install/ \
2. Install **docker-compose**: https://docs.docker.com/compose/install/

3. Run command in terminal:
> To execute the following commands you need to be in the root of the project
> 
>Для выполнения указанных команд необходимо перейти в корневую директорию проекта (*cd path/to/project*)

3.1 Build containers:
```
docker-compose up --build
```
#### URLs ###
FastApi Swagger: http://localhost:8080/docs
