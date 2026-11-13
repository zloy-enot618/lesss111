from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Клуб будующего.")
templates = Jinja2Templates(directory="templates")

events = [
    {
        "id": 1,
        "title": "Создание игр",
        "direction": "Геймдев",
        "seats": 5,
        "status": "Открыта"
    },
    {
        "id": 2,
        "title": "Воздушная автомагистраль",
        "direction": "Автодело",
        "seats": 476,
        "status": "Закрыта"
    },
    {
        "id": 3,
        "title": "Космический беговой путь",
        "direction": "Космонавтика",
        "seats": 3,
        "status": "Открыта"
    },
    {
        "id": 4,
        "title": "Подземные шахты",
        "direction": "Шахты",
        "seats": 687,
        "status": "Закрыта"
    }
]

class Event(BaseModel):
    id: int
    title: str
    direction: str
    seats: int
    status: str

@app.get("/api/events", response_model=list[Event])
def get_events():
    return events

@app.get("/api/events/open", response_model=list[Event])
def get_opened():
    result = []
    for event in events:
        if event["status"] == "Открыта":
            result.append(event)
    return result


@app.get("/", response_class=HTMLResponse)
def get_index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"events": events}
    )


