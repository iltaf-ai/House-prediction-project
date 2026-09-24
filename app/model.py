from sqlalchemy import Column , ForeignKey , Integer , Index , String  , Float 
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer , Index)
    email = Column(String(90) , unique = True , nullable =False )
    password = Column(String(90) , nullable= False)



class Predictions(Base):
    __tablename__ =  "Predictions"
    id = Column(Index , Integer)
    user_id = Column(Integer, ForeignKey("User.id") , nullable = False)
    Square_Footage =Column(Float) 
    Num_Bedrooms = Column(Float)
    Num_Bathrooms = Column(Float)
    Year_Built = Column(Float)
    Lot_Size  = Column(float)
    Garage_Size = Column(float)
    Neighborhood_Quality = Column(float)

    user= relationship("User" , back_populates="predictions")