from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes.auth import auth_router
from app.routes.dashboard import home_router
from app.routes.predict import predict_router 

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name = "static"
)


templates = Jinja2Templates(directory="app/templates")


app.include_router(auth_router)
app.include_router(home_router)
app.include_router(predict_router)

