# services/transcriber.py

import subprocess
import os
from config.settings import get_settings

settings = get_settings()

def transcribe_audio(audio_path: str) -> str:
    """
    Ejecuta whisper.cpp desde línea de comandos para transcribir un archivo de audio.

    Args:
        audio_path (str): Ruta al archivo de audio WAV o MP3.

    Returns:
        str: Ruta del archivo de texto generado con la transcripción.
    """
    whisper_exe = settings.whisper_path
    model_path = settings.whisper_model
    output_dir = settings.transcription_dir

    os.makedirs(output_dir, exist_ok=True)

    command = [
        whisper_exe,
        "-m", model_path,
        "-f", audio_path,
        "-otxt",
        "-of", os.path.join(output_dir, "transcription")
    ]

    print(f"📝 Ejecutando whisper:\n{' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("❌ Error en whisper:")
        print(result.stderr)
        raise RuntimeError("Whisper.cpp falló.")

    transcript_path = os.path.join(output_dir, "transcription.txt")
    print(f"✅ Transcripción completada: {transcript_path}")
    return transcript_path
 