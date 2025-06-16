# services/tts/utils_tts.py

import textwrap

def dividir_texto(texto: str, max_chars: int = 200):
    """
    Divide un texto largo en fragmentos más cortos, respetando límites de caracteres.
    """
    return textwrap.wrap(texto, width=max_chars, break_long_words=False)
