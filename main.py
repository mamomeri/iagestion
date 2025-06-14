# main.py

import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from fastapi import FastAPI
from api.routes import router



# Asegurar importaciones desde el directorio base
sys.path.append(os.path.dirname(__file__))

app = FastAPI(
    title="IA Gestión",
    description="API que integra reconocimiento de voz, síntesis de voz, y chat con LMS",
    version="1.0.0"
)

# CORS (útil si conectas desde un frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(router)
