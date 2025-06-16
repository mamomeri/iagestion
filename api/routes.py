# ruta: api/routes.py

import os
from fastapi import APIRouter
from api.schemas import TranscribeRequest, TTSRequest, CalcRequest
from services.transcriber import transcribe_audio
from services.calculator import evaluate_expression
from services.lms_client import chat_with_lms
from utils.audio import grabar_audio
from config.settings import get_settings
from services.tts.base_engine import reproducir_texto # ✅ Usa sistema unificado de TTS

router = APIRouter()
settings = get_settings()


@router.post("/transcribe")
def transcribe(req: TranscribeRequest):
    return {"text": transcribe_audio(req.file_path)}


@router.post("/speak")
def speak(req: TTSRequest):
    reproducir_texto(req.text, reproducir=False)
    return {"status": "ok", "mensaje": req.text}


@router.post("/chat")
def chat(req: TTSRequest):
    respuesta = chat_with_lms(req.text)
    return {"response": respuesta}


@router.post("/calculate")
def calculate(req: CalcRequest):
    return {"result": evaluate_expression(req.expression)}


@router.get("/record_and_transcribe")
def record_and_transcribe():
    audio_path = os.path.join(settings.audio_input_dir, "grabacion.wav")
    grabar_audio(audio_path, duracion=5)

    # Transcribe y responde con LMS
    lms_response = transcribe_audio(audio_path)

    return {
        "status": "ok",
        "audio_file": audio_path,
        "lms_response": lms_response
    }


@router.get("/listen_and_talk")
def listen_and_talk():
    audio_path = os.path.join(settings.audio_input_dir, "grabacion.wav")

    # 🎙️ Grabar (incluye sonidos de inicio/fin)
    grabar_audio(audio_path, duracion=5)

    # 🧠 Transcribir y enviar al LMS
    respuesta = transcribe_audio(audio_path)

    # 🔊 Leer con sistema TTS modular
    reproducir_texto(respuesta, reproducir=True)

    return {
        "status": "ok",
        "mensaje": respuesta
    }
