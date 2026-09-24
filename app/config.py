import os
from dotenv import load_dotenv

load_dotenv()


class setting():
    DATABASE = os.getenv("DATABASE_URL")
    ALGORITHM = os.getenv("ALGORITHM")
    SECRET_KEY = os.getenv("SECRET_KEY")
    TIME_TOKEN_EXPIRE = os.getenv("TIME_TOKEN_EXPIRE")

setting = setting()
