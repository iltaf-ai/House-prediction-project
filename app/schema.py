from pydantic import BaseModel , EmailStr , str , float


class UserCreate(BaseModel):
    email : EmailStr 
    password : str



class LoginUser(UserCreate):
    pass


class PredictionCreate(BaseModel):
        Square_Footage : float
        Num_Bedrooms : float
        Num_Bathrooms : float
        Year_Built : float
        Lot_Size   : float
        Garage_Size : float
        Neighborhood_Quality : float


class PredictionOut(PredictionCreate):
    id  : int
    user_id : int

   
    class Config:
        from_attributes = True

