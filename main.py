from fastapi import FastAPI, Depends, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from functools import lru_cache
from translator import translate_input
from dall_e_api import call_dall_e
from pathlib import Path
import config

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/server-status")
async def server_status(settings: config.Settings = Depends(get_settings)):
    return {"message": "Server ready", "app_name": settings.app_name}


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/images", response_class=HTMLResponse)
async def images(request: Request, text: str = Form(), settings: config.Settings = Depends(get_settings)):
    translated_text = translate_input(text)
    api_response = call_dall_e(translated_text, settings.api_key)
    return templates.TemplateResponse("carousel.html", {"request": request, "data": api_response.data})
