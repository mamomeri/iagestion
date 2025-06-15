# ruta: config/settings.py
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    whisper_path: str
    whisper_model: str
    tts_model_path: str
    tts_engine: str  # "xtts" o "tacotron"
    lms_endpoint: str
    audio_input_dir: str
    audio_output_dir: str
    transcription_dir: str

    class Config:
        env_file = "./config/.env"

@lru_cache()
def get_settings():
    return Settings()
