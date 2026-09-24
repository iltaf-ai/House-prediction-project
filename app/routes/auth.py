from fastapi import Depends, HTTPException, APIRouter , status
from app.schema import UserCreate
from app.model import User
from app.database import get_db
from sqlalchemy.orm import Session
from app.depencies import hash_password , verify_password , get_current_user, create_token
from app.schema import UserCreate , LoginUser
from fastapi.requests import Request
from fastapi.responses  import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="app/templates")
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



@auth_router.post("/login")
def login(user :LoginUser  , 
          db:Session = Depends(get_db)):

    user_db = db.query(User).filter(User.email == user.email).first()

    if not user_db:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid email or password"
        )
     

    if not  verify_password(user.password , user_db.password):
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="password worng"
        )

    token = create_token({"email" : user_db.email})

    return {
        "access_token": token,
        "token_type": "bearer",
        "message": "Login successful"
    }



@auth_router.post("/logout")
def logout(user = Depends(get_current_user) , db:Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid User"
        )
    db.delete(db_user)
    db.commit()



@auth_router.get("/register" , response_class=HTMLResponse)
def register_page(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html"
    )


@auth_router.get("/login" , response_class=HTMLResponse)
def login_page(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )