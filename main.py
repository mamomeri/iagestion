import os
import sys
import shutil
import simpleaudio as sa
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

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔄 Limpiar directorios + 🔊 reproducir audio de sistema listo
@app.on_event("startup")
def limpiar_directorios_audio():
    directorios = [
        os.path.join("Data", "audio_output"),
        os.path.join("Data", "audio_input"),
        os.path.join("Data", "transcripts")
    ]
    for output_dir in directorios:
        if os.path.exists(output_dir):
            for archivo in os.listdir(output_dir):
                archivo_path = os.path.join(output_dir, archivo)
                if output_dir == os.path.join("Data", "audio_input") and archivo == "speaker.wav":
                    continue
                try:
                    if os.path.isfile(archivo_path) or os.path.islink(archivo_path):
                        os.unlink(archivo_path)
                    elif os.path.isdir(archivo_path):
                        shutil.rmtree(archivo_path)
                except Exception as e:
                    print(f"Error al eliminar {archivo_path}: {e}")

    # 🔊 Reproducir sonido SystemAlready.wav
    try:
        ruta_audio = os.path.join("utils", "media", "audio", "SystemAlready.wav")
        wave_obj = sa.WaveObject.from_wave_file(ruta_audio)
        wave_obj.play()
        print("✅ Sistema listo para recibir órdenes.")
    except Exception as e:
        print(f"⚠️ No se pudo reproducir el sonido de inicio: {e}")

# Rutas
app.include_router(router)
