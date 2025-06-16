import simpleaudio as sa
import os
import sounddevice as sd
import scipy.io.wavfile as wav

def reproducir_sonido(nombre_archivo: str):
    """
    Reproduce un archivo de sonido desde utils/media/audio sin bloquear el hilo principal.
    """
    ruta = os.path.join("utils", "media", "audio", nombre_archivo)
    try:
        wave_obj = sa.WaveObject.from_wave_file(ruta)
        play_obj = wave_obj.play()
        return play_obj  # opcionalmente: play_obj.wait_done()
    except Exception as e:
        print(f"❌ Error al reproducir {nombre_archivo}: {e}")

def reproducir_wav(ruta_archivo: str):
    """
    Reproduce un archivo WAV completo desde una ruta específica.
    """
    try:
        wave_obj = sa.WaveObject.from_wave_file(ruta_archivo)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except Exception as e:
        print(f"❌ Error al reproducir {ruta_archivo}: {e}")

def grabar_audio(ruta_archivo: str, duracion: int = 4, fs: int = 16000):
    """
    Graba audio desde el micrófono, reproduce señales de inicio y fin, y guarda el archivo WAV.
    """
    reproducir_sonido("UserStartToSpeak.wav")
    print(f"🎙️ Grabando {duracion} segundos de audio...")
    audio = sd.rec(int(duracion * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    reproducir_sonido("UserStopSpeak.wav")
    wav.write(ruta_archivo, fs, audio)
    print(f"✅ Audio guardado en: {ruta_archivo}")
