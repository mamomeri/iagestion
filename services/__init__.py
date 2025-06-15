# ruta: services/tts/__init__.py

from config.settings import get_settings
settings = get_settings()

if settings.tts_engine.lower() == "xtts":
    from services.tts.xtts_engine import synthesize_text
elif settings.tts_engine.lower() == "tacotron":
    from services.tts.tacotron_engine import synthesize_text
else:
    raise ValueError(f"TTSEngine desconocido: {settings.tts_engine}")
