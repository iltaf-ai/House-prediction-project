from sqlalchemy import Column , ForeignKey , Integer , Index , String  , Float 
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer ,Index, primary_key=True )
    email = Column(String(90) , unique = True , nullable =False )
    password = Column(String(90) , nullable= False)



class Predictions(Base):
    __tablename__ =  "Predictions"
    id = Column(Integer , Index ,primary_key=True )
    user_id = Column(Integer, ForeignKey("users.id") , nullable = False)
    Square_Footage =Column(Integer) 
    Num_Bedrooms = Column(Integer)
    Num_Bathrooms = Column(Integer)
    Year_Built = Column(Integer)
    Lot_Size  = Column(Float)
    Garage_Size = Column(Integer)
    Neighborhood_Quality = Column(Integer)
    Predicted_Price = Column(Float)

    user= relationship("users" , back_populates="predictions")