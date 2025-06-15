# Guía de Motores de TTS en `services/tts/`

Este documento explica cómo funcionan los motores de TTS (texto a voz) en el sistema `IAGestion`, y cómo agregar uno nuevo de forma modular sin afectar el resto del código.

---

## 🏗️ Estructura Modular

La carpeta `services/tts/` contiene un archivo de enrutamiento `tts.py` que delega la función `synthesize_text()` al motor adecuado, según el valor definido en `.env`:

```ini
# config/.env
TTS_ENGINE=xtts
```

```python
# services/tts.py
if settings.tts_engine == "xtts":
    from services.tts.xtts_engine import synthesize_text
elif settings.tts_engine == "tacotron":
    from services.tts.tacotron_engine import synthesize_text
```

---

## 🤖 Motores Disponibles

### 1. `xtts_engine.py`

* Requiere `config.json`, `model.pth`, y `speaker.wav`
* Usa `XTTS` de Coqui.
* Permite clonación de voz (si se proporciona `speaker_wav`)

### 2. `tacotron_engine.py`

* Usa `speechbrain/tts-tacotron2-ljspeech` + `HiFi-GAN` como vocoder.
* No clona voz.
* Rápido y ligero.
* Compatible con Windows (sin symlinks).

---

## ➕ Agregar un Nuevo Motor TTS

1. **Crear archivo nuevo en `services/tts/`, ej: `myengine.py`**

   * Debe tener una función llamada `synthesize_text(text: str, language: str = "es", reproducir: bool = True)`.

2. **Actualizar `tts.py`** para enrutar correctamente:

   ```python
   elif settings.tts_engine == "myengine":
       from services.tts.myengine import synthesize_text
   ```

3. **Cambiar `.env`:**

   ```ini
   TTS_ENGINE=myengine
   ```

---

## 🔍 Detalles técnicos

* Todos los motores deben devolver `folder_name` con los audios en formato `.wav`, nombrados secuencialmente (`00001.wav`, `00002.wav`, ...)
* Opcionalmente reproducen el audio si `reproducir=True`.
* Los fragmentos se generan cortando el texto cada 30 caracteres aprox. para fluidez y control.

---

## 🚀 Ejemplo de uso

```bash
curl -X POST http://localhost:8000/speak \
    -H "Content-Type: application/json" \
    -d '{"text": "Hola, esta es una prueba."}'
```

Respuesta:

```json
{
  "status": "ok",
  "output_folder": "Data/audio_output/tts_20250614_231003",
  "files": ["00001.wav"]
}
```

---

## 🚪 Recomendaciones

* No sobrescribas `synthesize_text` directamente en `tts.py`. Solo importa desde motores.
* Agrega tus nuevos motores como archivos independientes.
* Puedes tener motores locales o desde `HuggingFace`.

---

👤 Autor: Marcos Moreira
