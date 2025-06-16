from TTS.api import TTS
from services.tts.utils_generacion import generar_wavs_desde_texto


MODEL = "tts_models/es/css10/vits"
OUTPUT_DIR = "Data/audio_output"

tts = TTS(MODEL)

def vits_speak(text: str, reproducir: bool = True) -> str:
    return generar_wavs_desde_texto(text, tts, OUTPUT_DIR, reproducir)
