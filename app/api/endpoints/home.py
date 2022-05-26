from fastapi import APIRouter
from utils.worker_tasks import load_csv_data
router = APIRouter()

@router.get("/")
async def home():
    # a dummy task call
    d = load_csv_data.delay()
    return 'Hello World'