# services/lms_client.py

import requests
from config.settings import get_settings

settings = get_settings()

def chat_with_lms(prompt: str) -> str:
    """
    Envía un prompt al modelo LMS u Ollama y devuelve la respuesta generada.

    Args:
        prompt (str): Texto de entrada.

    Returns:
        str: Respuesta generada por el modelo.
    """
    url = settings.lms_endpoint

    payload = {
        "model": "default",  # o el nombre de tu modelo en Ollama
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()

        # Adaptarse si estás usando Ollama directamente o LMS alternativo
        return result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()

    except requests.RequestException as e:
        print(f"❌ Error al comunicarse con LMS: {e}")
        return "Error al comunicarse con el modelo LMS."
