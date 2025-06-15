import os
import sys
import shutil
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

# Asegurar importaciones desde el directorio base
sys.path.append(os.path.dirname(__file__))

app = FastAPI(
    title="IA Gestión",
    description="API que integra reconocimiento de voz, síntesis de voz y chat con LMS",
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

# Borrar el contenido de Data/audio_output al iniciar la app
@app.on_event("startup")
def limpiar_directorios_audio():
    directorios = [os.path.join("Data", "audio_output"), os.path.join("Data", "audio_input")]
    for output_dir in directorios:
        if os.path.exists(output_dir):
            for archivo in os.listdir(output_dir):
                archivo_path = os.path.join(output_dir, archivo)
                try:
                    if os.path.isfile(archivo_path) or os.path.islink(archivo_path):
                        os.unlink(archivo_path)
                    elif os.path.isdir(archivo_path):
                        shutil.rmtree(archivo_path)
                except Exception as e:
                    print(f"Error al eliminar {archivo_path}: {e}")

# Rutas
app.include_router(router)
