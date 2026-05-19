from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / '.env')

class Settings:
    MONGODB_URL: str = os.getenv('MONGODB_URL', 'mongodb://mongodb:27017/ksi_bangladesh?authSource=admin')
    DB_NAME: str = os.getenv('DB_NAME', 'ksi_bangladesh')
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'replace-with-a-secure-random-key')
    ALGORITHM: str = os.getenv('ALGORITHM', 'HS256')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', '60'))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv('REFRESH_TOKEN_EXPIRE_DAYS', '7'))
    FRONTEND_URL: str = os.getenv('FRONTEND_URL', 'http://localhost')
    ADMIN_EMAIL: str = os.getenv('ADMIN_EMAIL', 'admin@ksibangladesh.com')
    ADMIN_PASSWORD: str = os.getenv('ADMIN_PASSWORD', 'Admin1234')
    MONGO_INITDB_ROOT_USERNAME: str = os.getenv('MONGO_INITDB_ROOT_USERNAME', 'root')
    MONGO_INITDB_ROOT_PASSWORD: str = os.getenv('MONGO_INITDB_ROOT_PASSWORD', 'example')

settings = Settings()
