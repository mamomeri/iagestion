import os
import torch
import soundfile as sf
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
from config.settings import get_settings

# Cargar configuración desde el entorno
settings = get_settings()

# Usar rutas relativas del .env
config_path = os.path.join(settings.tts_model_path, "config.json")
checkpoint_dir = settings.tts_model_path  # aquí vive model.pth

# Mostrar rutas para depuración
print("Ruta del modelo XTTS:", os.path.join(checkpoint_dir, "model.pth"))
print("Ruta de configuración:", config_path)

# Cargar la configuración y el modelo
config = XttsConfig()
config.load_json(config_path)
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir=checkpoint_dir, eval=True)
model.to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

# Función requerida por routes.py
def synthesize_text(text: str, speaker_wav: str = None, language: str = "es"):
    output_path = "output.wav"
    wav = model.synthesize(
        text,
        config,
        speaker_wav=speaker_wav,
        gpt_cond_len=3,
        language=language,
    )["wav"]
    sf.write(output_path, wav, 24000)
    return output_path
