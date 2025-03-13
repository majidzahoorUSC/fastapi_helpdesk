from fastapi import FastAPI
from app.models import models
from .utils.database import engine
from .routers import tickets

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(tickets.router)
