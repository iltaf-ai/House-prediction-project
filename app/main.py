from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.auth import auth_router
from app.routes.home import home_router
from app.routes.predict import predict_router 

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name = "static"
)




app.include_router(auth_router)
app.include_router(home_router)
app.include_router(predict_router)

