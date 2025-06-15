# 🧠 IAGestion

IAGestion es una aplicación modular de asistencia inteligente que combina reconocimiento de voz (`Whisper.cpp`), síntesis de voz (`Coqui TTS`), procesamiento de lenguaje natural (usando modelos de lenguaje como los de `LM Studio`) y funciones extendidas como una calculadora. Está pensado para ser una base extensible para proyectos de voz a texto, texto a voz y agentes conversacionales.

---

## 📁 Estructura del Proyecto

```
.
├── main.py                    # Arranque principal del backend
├── README.md
├── requirements.txt
│
├── api/                       # Endpoints de FastAPI
│   └── routes.py              # /transcribe, /speak, /calculate
│
├── config/                   # Configuración y .env
│   ├── .env
│   ├── settings.py
│
├── services/                 # Lógica de negocio
│   ├── transcriber.py        # Controla Whisper
│   ├── tts.py                # Controla Coqui TTS
│   ├── lms_client.py         # Controla LMS (Local Model Server)
│   └── calculator.py
│
├── Models/                   # Modelos externos
│   ├── whisper/
│   │   ├── ggml-large-v3-turbo-q8_0.bin
│   │   └── Release/          # Binarios compilados de whisper.cpp
│   └── tts/
│       └── Models/xtts_v2    # Ruta al modelo de TTS
│
├── Data/                     # Archivos de entrada/salida
│   ├── audio_input/          # Archivos grabados de micrófono
│   ├── audio_output/         # Resultados de TTS generados
│   └── transcriptions/       # Texto transcrito por Whisper
│
└── utils/
    └── audio.py              # Grabación de micrófono
```

---

## ⚙️ Requisitos

- Python **3.10**
- Dependencias de `requirements.txt`
- CUDA opcional si deseas usar `ggml-cuda.dll` para Whisper

Instala entorno virtual:

```bash
py -3.10 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔐 Variables de entorno

Edita `config/.env`:

```
WHISPER_PATH=./Models/whisper/Release/main.exe
WHISPER_MODEL=./Models/whisper/ggml-large-v3-turbo-q8_0.bin
TTS_MODEL_PATH=./Models/tts/Models/xtts_v2
LMS_ENDPOINT=http://127.0.0.1:1234/v1/chat/completions

AUDIO_INPUT_DIR=./Data/audio_input
AUDIO_OUTPUT_DIR=./Data/audio_output
TRANSCRIPTION_DIR=./Data/transcriptions
```

---

## 🚀 Cómo ejecutar

Ejecuta con:

```bash
python start.py
```

Esto lanza una API FastAPI + una prueba local de grabación/transcripción al micrófono si está configurado.

---

## 🔉 Funciones API

| Endpoint        | Método | Descripción                        |
|-----------------|--------|------------------------------------|
| `/transcribe`   | POST   | Transcribe un archivo de audio     |
| `/speak`        | POST   | Convierte texto en voz con Coqui   |
| `/calculate`    | POST   | Calcula expresiones matemáticas    |

---

## 🧪 Ejemplo de uso

```python
import requests

# Transcripción
r = requests.post("http://localhost:8000/transcribe", json={"file_path": "Data/audio_input/test.wav"})
print(r.json())

# Texto a voz
r = requests.post("http://localhost:8000/speak", json={"text": "Hola, soy tu asistente de voz"})
with open("output.wav", "wb") as f:
    f.write(r.content)
```

---

## 🧠 Arquitectura y Rol como Gestor

Este proyecto **no es solo una API**, sino un **gestor modular de servicios de voz y lenguaje**, fácilmente ampliable con nuevas funcionalidades. Su diseño desacoplado permite integrar nuevos modelos o servicios sin alterar el núcleo de rutas.

Cada módulo (STT, TTS, NLP, cálculo) es llamado de forma independiente a través de una **interfaz REST**, facilitando la integración con frontends web, asistentes virtuales o automatizaciones.

---

## 🛠️ TODOs

- [ ] Documentar uso de modelos múltiples
- [ ] Agregar autenticación por token
- [ ] Interfaz web en React o HTML simple
- [ ] Soporte multi-idioma

---

## 🤝 Contribuciones

Puedes usar esta estructura como base para agentes de IA, asistentes personales, asistentes educativos o módulos de automatización por voz.

---

## 🧠 Autor

**Marcos Moreira** – Proyecto personal orientado a la integración realista de IA con voz y asistencia lógica.
