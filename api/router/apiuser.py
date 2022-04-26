from fastapi import APIRouter , Body
from models.user import User
from typing import List


router = APIRouter()

users=[]
@router.post("" , name="Student")
def school(payload : dict= Body(...)):
    user = payload.get("username")
    return {"username" : user }

@router.post('/signup',status_code=201)
def create_user(user:User):
    new_user={
        "username":user.username,
        "email":user.email,
        "password":user.password
    }

    users.append(new_user)

    return new_user

#getting all users
@router.get('/users',response_model=List[User])
def get_users():
    return users