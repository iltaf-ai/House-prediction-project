from fastapi import Depends, HTTPException, APIRouter
from app.schema import UserCreate
from app.model import User
from app.database import get_db
from sqlalchemy.orm import Session
from app.depencies import hash_password , verify_password , get_current_user


auth_router = APIRouter()


@auth_router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    user_existing = db.query(User).filter(User.email == user.email).first()

    if user_existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully", "email": new_user.email}