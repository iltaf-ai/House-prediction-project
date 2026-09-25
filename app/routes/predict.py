from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schema import PredictionCreate
from app.model import Predictions
from app.database import get_db
from app.depencies import get_current_user
from app.notebooks import Pipeline_model

prediction_router = APIRouter()


@prediction_router.post("/prediction")
def prediction(
    user: PredictionCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    new_input = [[
        user.Square_Footage,
        user.Num_Bedrooms,
        user.Num_Bathrooms,
        user.Year_Built,
        user.Lot_Size,
        user.Garage_Size,
        user.Neighborhood_Quality
        
    ]]

    predicted_price = Pipeline_model.predict(new_input)[0]

    new_prediction = Predictions(
        Square_Footage=user.Square_Footage,
        Num_Bedrooms=user.Num_Bedrooms,
        Num_Bathrooms=user.Num_Bathrooms,
        Year_Built=user.Year_Built,
        Lot_Size=user.Lot_Size,
        Garage_Size=user.Garage_Size,
        Neighborhood_Quality=user.Neighborhood_Quality,
        Predicted_Price=predicted_price,
        user_id=current_user.id
    )

    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)

    return {
        "message": "Prediction saved successfully",
        "predicted_price": predicted_price
    }