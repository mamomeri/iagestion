# utils/audio.py

import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np

def grabar_audio(ruta_archivo: str, duracion: int = 4, fs: int = 16000):
    """
    Graba audio del micrófono y lo guarda en un archivo WAV.

    Args:
        ruta_archivo (str): Ruta de salida para el archivo .wav.
        duracion (int): Duración de la grabación en segundos (por defecto 4).
        fs (int): Frecuencia de muestreo en Hz (por defecto 16000).
    """
    print(f"🎙️ Grabando {duracion} segundos de audio...")
    audio = sd.rec(int(duracion * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write(ruta_archivo, fs, audio)
    print(f"✅ Audio guardado en: {ruta_archivo}")
