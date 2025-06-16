# utils/audio_check.py

import os
import soundfile as sf
import librosa

AUDIO_INPUT_DIR = "../Data/audio_input"

def verificar_y_convertir_audios(sobrescribir: bool = True):
    for archivo in os.listdir(AUDIO_INPUT_DIR):
        if archivo.endswith(".wav"):
            ruta = os.path.join(AUDIO_INPUT_DIR, archivo)
            print(f"\n🔍 Analizando: {archivo}")

            datos, sr = sf.read(ruta, always_2d=False)
            canales = 1 if datos.ndim == 1 else datos.shape[1]
            tipo = datos.dtype if hasattr(datos, 'dtype') else type(datos)
            duracion = librosa.get_duration(y=datos, sr=sr)

            print(f"  • Frecuencia: {sr} Hz")
            print(f"  • Canales: {'Mono' if canales == 1 else 'Stereo'}")
            print(f"  • Tipo: {tipo}")
            print(f"  • Duración: {duracion:.2f} s")

            necesita_conversion = sr != 16000 or canales != 1 or tipo != 'int16'
            if necesita_conversion and sobrescribir:
                print("  ⚠️ No compatible. Convirtiendo y sobrescribiendo...")
                datos, _ = librosa.load(ruta, sr=16000, mono=True)
                datos_int16 = (datos * 32767).astype("int16")
                sf.write(ruta, datos_int16, 16000)
                print("  ✅ Conversión completada.")
            elif necesita_conversion:
                print("  ⚠️ No compatible. (No se sobrescribió)")
            else:
                print("  ✅ Compatible.")

if __name__ == "__main__":
    verificar_y_convertir_audios(sobrescribir=True)
