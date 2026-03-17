from fastapi import FastAPI, Request, Form
from typing import Annotated
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class UserRegistration(BaseModel):
    email: str
    password: str


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) 

@app.get("/account")
async def account(request: Request):
    return templates.TemplateResponse("account.html", {"request": request})

@app.post("/login/")
async def login(email: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"email": email, "password":password}
    
