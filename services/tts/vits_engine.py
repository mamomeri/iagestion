import os
import torch
import soundfile as sf
import textwrap
import time
import simpleaudio as sa
from datetime import datetime
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

from config.settings import get_settings

# Configuración general
settings = get_settings()

tts_dir = os.path.join(settings.tts_model_path, "vits_es")
os.makedirs(tts_dir, exist_ok=True)

# Descargar modelo VITS en español (sin clonar voz)
manager = ModelManager()
model_path, config_path, model_item = manager.download_model("tts_models/es/css10/vits")

# Inicializar el sintetizador
synthesizer = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
    use_cuda=torch.cuda.is_available(),
)

# Fragmentador de texto
def dividir_texto(texto, max_chars=110):
    return textwrap.wrap(texto, width=max_chars, break_long_words=False)

# Función principal
def synthesize_text(text: str, language: str = "es", reproducir: bool = True):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = os.path.join("Data", "audio_output", f"vits_{timestamp}")
    os.makedirs(folder_name, exist_ok=True)

    fragmentos = dividir_texto(text)
    archivos = []

    for i, fragmento in enumerate(fragmentos):
        wav = synthesizer.tts(fragmento)
        nombre_archivo = os.path.join(folder_name, f"{i+1:05}.wav")
        sf.write(nombre_archivo, wav, 22050)
        archivos.append(nombre_archivo)

        if reproducir:
            wave_obj = sa.WaveObject.from_wave_file(nombre_archivo)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            time.sleep(0.2)

    return folder_name
