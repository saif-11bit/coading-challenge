from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from application import templates

router = APIRouter()

@router.get("/{id}", response_class=HTMLResponse)
async def display_chart(request: Request, id: str):
    return templates.TemplateResponse("chart.html", {"request": request, "id": id})