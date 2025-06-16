from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
from utils.audio import reproducir_wav
import os
import tempfile

def generar_wavs_desde_texto(texto: str, tts_model, output_dir: str, reproducir: bool = True) -> str:
    """
    Genera un archivo WAV con el texto dado usando un modelo tts_model.
    """
    os.makedirs(output_dir, exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".wav", dir=output_dir, delete=False) as f:
        path_salida = f.name
    tts_model.tts_to_file(text=texto, file_path=path_salida)
    if reproducir:
        reproducir_wav(path_salida)
    return path_salida
