import os
from services.tts.espeak_engine import espeak_speak, limpiar_texto_para_espeak
# Cargar .env de forma explícita antes de leer variables
from dotenv import load_dotenv
load_dotenv(dotenv_path="./config/.env")
engine = os.environ.get("TTS_ENGINE", "tacotron2")
print(f"Motor TTS seleccionado desde .env: {engine}")

def synthesize_text(texto: str, reproducir: bool = True) -> str:
    if engine == "espeak":
        texto = limpiar_texto_para_espeak(texto)
        return espeak_speak(texto, reproducir=reproducir)
    elif engine == "tacotron2":
        from services.tts.tacotron_engine import tacotron_speak
        return tacotron_speak(texto, reproducir=reproducir)
    elif engine == "vits":
        from services.tts.vits_engine import vits_speak
        return vits_speak(texto, reproducir=reproducir)
    elif engine == "xtts":
        from services.tts.xtts_engine import xtts_speak
        return xtts_speak(texto, reproducir=reproducir)
    else:
        raise ValueError(f"Motor TTS desconocido: {engine}")
