from fastapi import APIRouter
from api.router import apiuser


router = APIRouter() 
router.include_router(apiuser.router, tags=["apiuser"], prefix="/apiuser")
