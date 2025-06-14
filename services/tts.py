from TTS.api import TTS
from config.settings import get_settings
import os

settings = get_settings()

config_path = os.path.join(settings.tts_model_path, "config.json")
model_path = os.path.join(settings.tts_model_path, "model.pth")

print("Ruta del modelo TTS:", model_path)
print("Ruta de configuración TTS:", config_path)

tts = TTS(
    config_path=config_path,
    model_path=model_path,
    progress_bar=False,
    gpu=False
)

# Función requerida en routes.py
def synthesize_text(text: str, speaker_wav: str = None, language: str = "es"):
    output_path = "output.wav"
    wav = tts.tts(text, speaker_wav=speaker_wav, language=language)
    tts.save_wav(wav, output_path)
    return output_path
