import os
import torch
import soundfile as sf
import textwrap
import time
import simpleaudio as sa
from datetime import datetime

from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
from config.settings import get_settings

# Cargar configuración del entorno
settings = get_settings()
config_path = os.path.join(settings.tts_model_path, "config.json")
checkpoint_dir = settings.tts_model_path

# Cargar modelo XTTS
config = XttsConfig()
config.load_json(config_path)
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir=checkpoint_dir, eval=True)
model.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

# Divide el texto en fragmentos pequeños (evita recortes)
def dividir_texto(texto, max_chars=220):
    return textwrap.wrap(texto, width=max_chars, break_long_words=False)

# Función principal de síntesis sin clonación de voz
def synthesize_text(text: str, language: str = "es", reproducir: bool = False):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = os.path.join("Data", "audio_output", f"tts_{timestamp}")
    os.makedirs(folder_name, exist_ok=True)

    fragmentos = dividir_texto(text)
    archivos = []

    for i, fragmento in enumerate(fragmentos):
        wav = model.synthesize(
            fragmento,
            config=config,
            speaker_wav=None,           # 🔧 Este parámetro es obligatorio
            gpt_cond_len=3,
            language=language,
        )["wav"]

        nombre_archivo = os.path.join(folder_name, f"{i:03}.wav")
        sf.write(nombre_archivo, wav, 24000)
        archivos.append(nombre_archivo)

    if reproducir:
        for archivo in archivos:
            wave_obj = sa.WaveObject.from_wave_file(archivo)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            time.sleep(0.2)

    return folder_name
