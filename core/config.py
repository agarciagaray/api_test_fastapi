from pydantic import BaseSettings

class Settings(BaseSettings):
    MYSQL_URL: str = "mysql+pymysql://igdadmin:$User#Conec.2022$@localhost:3306/dbigdtemp_datastorage"
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_DAYS: int = 365

settings = Settings()