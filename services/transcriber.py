
import subprocess
import os
from config.settings import get_settings
from utils.audio_converter import convertir_a_wav

settings = get_settings()

def transcribe_audio(audio_path: str) -> str:
    """
    Ejecuta whisper.cpp desde línea de comandos para transcribir un archivo de audio.
    Convierte automáticamente a WAV compatible si es necesario.
    """
    whisper_exe = settings.whisper_path
    model_path = settings.whisper_model
    output_dir = settings.transcription_dir

    os.makedirs(output_dir, exist_ok=True)

    # Asegurar compatibilidad
    wav_path = convertir_a_wav(audio_path)

    command = [
        whisper_exe,
        "-m", model_path,
        "-f", wav_path,
        "-otxt",
        "-of", os.path.join(output_dir, "transcription")
    ]

    print(f"📝 Ejecutando whisper:\n{' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("❌ Error en whisper:")
        print("STDERR:\n", result.stderr)
        print("STDOUT:\n", result.stdout)
        raise RuntimeError("Whisper.cpp falló.")

    transcript_path = os.path.join(output_dir, "transcription.txt")
    print(f"✅ Transcripción completada: {transcript_path}")
    return transcript_path
