import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./config/.env")  # <- Esto debe estar antes de leer la variable

engine = os.environ.get("TTS_ENGINE", "tacotron2")
print(f"Motor TTS seleccionado desde .env: {engine}")

from .utils_tts import dividir_texto
from . import __init__  # Opcional si se usa `synthesize_text` directamente en otros módulos


def reproducir_texto(texto: str, reproducir: bool = True) -> str:
    from . import synthesize_text
    return synthesize_text(texto, reproducir=reproducir)
