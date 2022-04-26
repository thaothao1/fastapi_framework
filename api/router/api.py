from fastapi import APIRouter
from api.router import action


router = APIRouter() 

router.include_router(action.router, tags=["action"] , prefix="/action")