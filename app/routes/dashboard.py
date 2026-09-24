from fastapi import Depends , HTTPException , status , APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

tamplates = Jinja2Templates(directory="app/templates")


dashboard_router = APIRouter


@dashboard_router.get("/dashboard" , response_class=HTMLResponse)
def dashboard_page(request:Request):
    return tamplates.TemplateResponse(
        request=request,
        name = "dashboard.html"
    )


