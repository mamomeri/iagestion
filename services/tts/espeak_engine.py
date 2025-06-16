import subprocess
import tempfile
import re
import unicodedata

def limpiar_texto_para_espeak(texto: str) -> str:
    # Eliminar emojis y símbolos especiales
    texto = ''.join(c for c in texto if unicodedata.category(c)[0] != "S")

    # Eliminar URLs y markdown
    texto = re.sub(r"\[.*?\]\(.*?\)", "", texto)  # [texto](link)
    texto = re.sub(r"http[s]?://\S+", "", texto)  # enlaces

    # Permitir letras, números, puntuación básica
    texto = re.sub(r"[^a-zA-Z0-9áéíóúüÁÉÍÓÚÜñÑ.,()¿?¡! ]+", "", texto)

    # Reemplazar múltiples espacios por uno solo
    texto = re.sub(r"\s+", " ", texto).strip()
    
    return texto


def espeak_speak(texto: str, reproducir: bool = True) -> str:
    texto_limpio = limpiar_texto_para_espeak(texto)
    salida_wav = tempfile.mktemp(suffix=".wav")
    try:
        subprocess.run(
            ["espeak-ng", "-s", "150", "-p", "40", "-v", "es+f3", "-w", salida_wav, texto_limpio],

            check=True
        )
        if reproducir:
            subprocess.run(["ffplay", "-nodisp", "-autoexit", salida_wav], check=True)
        return salida_wav
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error al usar espeak-ng: {e}")
