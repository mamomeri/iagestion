# ruta: api/routes.py
import os
from fastapi import APIRouter
from api.schemas import TranscribeRequest, TTSRequest, CalcRequest
from services.transcriber import transcribe_audio
from services.tts import synthesize_text  # ✅ Solo desde aquí
from services.calculator import evaluate_expression
from services.lms_client import chat_with_lms
from utils.audio import grabar_audio
from config.settings import get_settings

router = APIRouter()
settings = get_settings()

@router.post("/transcribe")
def transcribe(req: TranscribeRequest):
    return {"text": transcribe_audio(req.file_path)}

@router.post("/speak")
def speak(req: TTSRequest):
    folder = synthesize_text(req.text)
    wav_files = sorted(f for f in os.listdir(folder) if f.endswith(".wav"))
    return {
        "status": "ok",
        "output_folder": folder,
        "files": wav_files
    }

@router.post("/calculate")
def calculate(req: CalcRequest):
    return {"result": evaluate_expression(req.expression)}

@router.post("/chat")
def chat(req: TTSRequest):
    return {"response": chat_with_lms(req.text)}

@router.get("/record_and_transcribe")
def record_and_transcribe():
    audio_path = os.path.join(settings.audio_input_dir, "grabacion.wav")
    grabar_audio(audio_path, duracion=5)
    transcript_path = transcribe_audio(audio_path)

    with open(transcript_path, "r", encoding="utf-8") as f:
        texto = f.read()

    return {
        "status": "ok",
        "audio_file": audio_path,
        "transcript_file": transcript_path,
        "transcription": texto
    }
