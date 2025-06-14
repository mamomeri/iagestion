# ruta: services/tts.py

from config.settings import get_settings

settings = get_settings()

if settings.tts_engine == "xtts":
    from services.tts.xtts_engine import synthesize_text
elif settings.tts_engine == "tacotron":
    from services.tts.tacotron_engine import synthesize_text
else:
    raise ValueError("Motor TTS no soportado. Usa 'xtts' o 'tacotron'.")
