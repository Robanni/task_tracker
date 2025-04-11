from fastapi import  APIRouter

from settings import Settings

router = APIRouter(prefix="/ping",tags=["ping"])    

@router.get("/db")
async def ping_db():
    return {"massage":"db is working"}

@router.get("/app")
async def ping_app():
    return {"text":"app is working"}