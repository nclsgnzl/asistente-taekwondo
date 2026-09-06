import os
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from slowapi import Limiter
from slowapi.util import get_remote_address
from rag import responder

load_dotenv()
APP_API_KEY = os.getenv("APP_API_KEY")

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pregunta(BaseModel):
    pregunta: str

@app.post("/preguntar")
@limiter.limit("10/minute")
def preguntar(request: Request, datos: Pregunta, x_api_key: str = Header(None)):
    if x_api_key != APP_API_KEY:
        raise HTTPException(status_code=401, detail="API key inválida")
    respuesta = responder(datos.pregunta)
    return {"respuesta": respuesta}

@app.get("/")
def health():
    return {"status": "ok"}