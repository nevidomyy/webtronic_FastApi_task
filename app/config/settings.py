import os

DB_HOST:str = 'webtronic_db'
POSTGRESQL_DSN: str = f'postgresql://webtronic:password@{DB_HOST}:5432/webtronic'
APP_NAME: str = 'Webtronic'
API_VERSION: str = '1.0'
APP_HOST: str = '0.0.0.0'
APP_PORT: int = 8080
API_DOCS_USER: str = 'admin'
API_DOCS_PASSWD: str = 'password'

# JWT config
JWT_AUTH_EXP_DELTA_SECONDS: int = 3600
JWT_REFRESH_EXP_DELTA_SECONDS: int = 604800
JWT_ALGORITHM: str = 'HS256'

# auth configuration
SECRET: str = os.getenv('SECRET', 'p0G9zGngfYpSwC0Lc3bDLe9ik9v4uJmMjS0OrCsoGA15IwO8qBltk8M2a8b42Us7NlId8122P6kSxlCz')
SALT: bytes = os.getenv('SALT', 'imhPkoKI6X4z8dT6RmJtYkx2bQD3mG4pk9MqpeA5WTTvdZLBz5').encode('utf-8')
