# from sqlalchemy import Column , Integer , String
# from database import Base

# class User(Base):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key = True , index = True)
#     name = Column(String)
from pydantic import BaseModel
class User(BaseModel):
    username:str
    email:str
    password:str

    class Config:
        schema_extra={
            "example":{
                "username":"john doe",
                "email":"johndoe@gmail.com",
                "password":"password"
            }
        }
