# ruta: utils/audio_check.py

import os
import soundfile as sf
import librosa
import numpy as np

def verificar_y_convertir_audios(directorio="../Data/audio_input", convertir=False):
    for archivo in os.listdir(directorio):
        if archivo.endswith(".wav"):
            ruta = os.path.join(directorio, archivo)
            print(f"\n🔍 Analizando: {archivo}")

            try:
                data, samplerate = sf.read(ruta)
                canales = 1 if len(data.shape) == 1 else data.shape[1]
                duracion = len(data) / samplerate
                tipo = data.dtype if hasattr(data, 'dtype') else type(data)

                print(f"  • Frecuencia: {samplerate} Hz")
                print(f"  • Canales: {'Mono' if canales == 1 else 'Estéreo'}")
                print(f"  • Tipo: {tipo}")
                print(f"  • Duración: {duracion:.2f} s")

                if convertir:
                    print("  ⚙️ Convirtiendo a mono / 16kHz / int16...")
                    # Cargar con librosa en mono, re-sampleado
                    data_conv, sr_conv = librosa.load(ruta, sr=16000, mono=True)
                    data_int16 = (data_conv * 32767).astype(np.int16)

                    nuevo_nombre = os.path.splitext(archivo)[0] + "_mono.wav"
                    nueva_ruta = os.path.join(directorio, nuevo_nombre)
                    sf.write(nueva_ruta, data_int16, 16000)
                    print(f"  ✅ Guardado como: {nuevo_nombre}")
            except Exception as e:
                print(f"  ❌ Error al procesar {archivo}: {e}")


verificar_y_convertir_audios()