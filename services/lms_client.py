# services/lms_client.py

import requests
from config.settings import get_settings

settings = get_settings()

def chat_with_lms(prompt: str) -> str:
    """
    Envía un prompt al modelo de LM Studio y devuelve la respuesta generada.

    Args:
        prompt (str): Texto de entrada.

    Returns:
        str: Respuesta generada por el modelo.
    """
    url = settings.lms_endpoint  # Debe ser http://localhost:1234/v1/chat/completions

    payload = {
        "model": "google/gemma-3-4b",  # 🧠 Especifica el modelo cargado en LM Studio
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()

        return result["choices"][0]["message"]["content"].strip()

    except requests.RequestException as e:
        print(f"❌ Error al comunicarse con LMS: {e}")
        return "Error al comunicarse con el modelo LMS."
