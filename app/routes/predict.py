from fastapi import HTTPException , Depends , status , APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from app.model import Predictions
from app.schema import PredictionCreate
from fastapi import UploadFile
from app.depencies import get_current_user
from sqlalchemy.orm  import Session
from app.database import get_db

prediction_router = APIRouter()

@prediction_router.post("/prediction")
def prediction(user : PredictionCreate , current_user = Depends(get_current_user) , db:Session = Depends(get_db)):
    Square_Footage = input("Entre you Square_Footage : ")
    Num_Bedrooms = input("Entre you Num_Bedrooms: ")
    Num_Bathrooms = input("Entre you Num_Bedrooms: ")
    
