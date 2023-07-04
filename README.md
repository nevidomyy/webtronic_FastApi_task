# FastAPI Posts APP Task
#### Supported JWT authorization
#### Software development stack ####
Fastapi - web framework\
SQLAlchemy - ORM\
Alembic - Migration manager\
Pydantic - Data and models validator.




#### Build and run ####
1. Install **docker**: https://docs.docker.com/engine/install/ 
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
> Use access jwt token to authorize in swagger