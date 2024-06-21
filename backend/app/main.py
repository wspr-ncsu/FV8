from fastapi import FastAPI,APIRouter
from app.api import tasks

api_router = APIRouter()
api_router.include_router(tasks.router)

app = FastAPI()
app.include_router(api_router, prefix='/api/v1')
