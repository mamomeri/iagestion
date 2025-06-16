import subprocess
import os
from config.settings import get_settings
from utils.audio_converter import convertir_a_wav
from services.lms_client import chat_with_lms  # 👈 Importación para comunicar con LMS

settings = get_settings()

def transcribe_audio(audio_path: str) -> str:
    """
    Ejecuta whisper.cpp desde línea de comandos para transcribir un archivo de audio.
    Convierte automáticamente a WAV compatible si es necesario y envía el texto al LMS.
    
    Args:
        audio_path (str): Ruta al archivo de audio (WAV, MP3, etc.)
    
    Returns:
        str: Respuesta del modelo LMS
    """
    whisper_exe = settings.whisper_path
    model_path = settings.whisper_model
    output_dir = settings.transcription_dir

    os.makedirs(output_dir, exist_ok=True)

    # ✅ Asegurar compatibilidad con whisper.cpp
    wav_path = convertir_a_wav(audio_path)

    # ✅ Ejecutar whisper con idioma forzado a español
    command = [
        whisper_exe,
        "-m", model_path,
        "-f", wav_path,
        "-otxt",
        "-l", "es",  # Forzar reconocimiento en español
        "-of", os.path.join(output_dir, "transcription")
    ]

    print(f"📝 Ejecutando whisper:\n{' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("❌ Error en whisper:")
        print("STDERR:\n", result.stderr)
        print("STDOUT:\n", result.stdout)
        raise RuntimeError("Whisper.cpp falló.")

    # ✅ Leer el texto generado
    transcript_path = os.path.join(output_dir, "transcription.txt")
    print(f"✅ Transcripción completada: {transcript_path}")

    with open(transcript_path, "r", encoding="utf-8") as f:
        texto = f.read()

    print(f"📜 Texto transcrito:\n{texto}")

    # ✅ Enviar al LMS y retornar la respuesta
    try:
        respuesta = chat_with_lms(texto)
        print(f"🧠 LMS respondió:\n{respuesta}")
        return respuesta
    except Exception as e:
        print(f"❌ Error al comunicarse con LMS: {e}")
        return "Error al comunicarse con el modelo LMS."
