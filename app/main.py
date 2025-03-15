from fastapi import FastAPI, Request
from app.models import models
from .utils.database import engine
from .routers import tickets
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(tickets.router)


# Absolute path to the templates directory
templates_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_dir)
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    message = "Hello, FastAPI with Templates!"
    # Render the index.html template
    return templates.TemplateResponse("index.html", {"request": request, "message": message})


