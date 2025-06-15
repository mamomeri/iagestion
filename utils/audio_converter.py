import os
import soundfile as sf
import numpy as np
from scipy.io.wavfile import write as wav_write
from scipy.signal import resample

def convertir_a_wav_compatible(origen: str, destino: str = None):
    """
    Convierte cualquier archivo de audio (WAV, MP3, FLAC...) a un WAV mono, 16kHz, int16.

    Args:
        origen (str): Ruta del archivo original.
        destino (str): Ruta del archivo convertido (opcional). Si no se especifica, se sobreescribe.
    """
    if not os.path.isfile(origen):
        raise FileNotFoundError(f"Archivo no encontrado: {origen}")

    data, sr = sf.read(origen)
    destino = destino or os.path.splitext(origen)[0] + "_converted.wav"

    # Convertir a mono si es estéreo
    if data.ndim > 1:
        data = np.mean(data, axis=1)

    # Resamplear si no está en 16000 Hz
    if sr != 16000:
        num_samples = int(len(data) * 16000 / sr)
        data = resample(data, num_samples)
        sr = 16000

    # Normalizar a rango [-1, 1] y convertir a int16
    if data.dtype != np.int16:
        data = data / np.max(np.abs(data)) if np.max(np.abs(data)) > 0 else data
        data = np.int16(data * 32767)

    # Guardar archivo WAV compatible
    wav_write(destino, sr, data)
    print(f"✅ Audio convertido a WAV compatible: {destino}")
    return destino
