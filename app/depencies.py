from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.config import setting
from app.model import User, Predictions
from app.schema import UserCreate, PredictionCreate
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.database import get_db
from sqlalchemy.orm import Session


SECRET_KEY = setting.SECRET_KEY
ALGORITHM = setting.ALGORITHM
TOKEN_TIME_EXPIRE = setting.TIME_TOKEN_EXPIRE



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
auth_schemes = OAuth2PasswordBearer(tokenUrl="login")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_TIME_EXPIRE)
    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verify_username(token: str = Depends(auth_schemes)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")

        if not email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token")
        return email

    
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate token")


def get_current_user(email: str = Depends(verify_username),
                      db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == email).first()
    
    if not user:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found")
    return user