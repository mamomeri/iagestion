# api/routes.py

from fastapi import APIRouter
from api.schemas import TranscribeRequest, TTSRequest, CalcRequest
from services.transcriber import transcribe_audio
from services.tts import synthesize_text
from services.calculator import evaluate_expression
from services.lms_client import chat_with_lms

router = APIRouter()

@router.post("/transcribe")
def transcribe(req: TranscribeRequest):
    return {"text": transcribe_audio(req.file_path)}

@router.post("/speak")
def speak(req: TTSRequest):
    synthesize_text(req.text)
    return {"status": "ok"}

@router.post("/calculate")
def calculate(req: CalcRequest):
    result = evaluate_expression(req.expression)
    return {"result": result}

@router.post("/chat")
def chat(req: TTSRequest):
    return {"response": chat_with_lms(req.text)}
