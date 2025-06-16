import os
from TTS.api import TTS
from utils.audio import reproducir_wav
from services.tts.utils_generacion import generar_wavs_desde_texto


MODEL = "tts_models/es/mai/tacotron2-DDC"
OUTPUT_DIR = "Data/audio_output"

tts = TTS(MODEL)

def tacotron_speak(text: str, reproducir: bool = True) -> str:
    return generar_wavs_desde_texto(text, tts, OUTPUT_DIR, reproducir)
