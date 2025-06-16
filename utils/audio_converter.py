# utils/audio_converter.py

import os
import librosa
import soundfile as sf

def convertir_a_wav(audio_path: str, destino_dir: str = "Data/audio_input") -> str:
    """
    Convierte cualquier archivo de audio a WAV mono 16kHz compatible con Whisper.cpp.
    
    Args:
        audio_path (str): Ruta al archivo original.
        destino_dir (str): Directorio donde guardar el archivo convertido.

    Returns:
        str: Ruta al archivo WAV listo para transcripción.
    """
    nombre = os.path.splitext(os.path.basename(audio_path))[0]
    destino_path = os.path.join(destino_dir, f"{nombre}_converted.wav")

    # Cargar con librosa (convierte a float32 y permite re-samplear)
    audio, sr = librosa.load(audio_path, sr=16000, mono=True)

    # Guardar en el formato esperado
    sf.write(destino_path, audio, 16000)
    print(f"✅ Convertido a WAV compatible: {destino_path}")
    return destino_path
