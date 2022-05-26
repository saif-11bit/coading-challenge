from fastapi import APIRouter
from utils.worker_tasks import create_task
router = APIRouter()

@router.get("/")
async def home():
    # a dummy task call
    d = create_task.delay(1, 2, 3)
    print(d)
    return 'Hello World'