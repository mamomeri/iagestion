# ruta: services/tts/__init__.py

from services.tts.tacotron_engine import synthesize_text as synthesize_tacotron
from services.tts.xtts_engine import synthesize_text as synthesize_xtts
from services.tts.vits_engine import synthesize_text as synthesize_vits

from config.settings import get_settings

settings = get_settings()

# Escoge el motor según configuración
engine_selector = {
    "tacotron": synthesize_tacotron,
    "xtts": synthesize_xtts,
    "vits": synthesize_vits
}

synthesize_text = engine_selector.get(settings.tts_engine, synthesize_tacotron)
