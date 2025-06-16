# api/schemas.py

from pydantic import BaseModel

class TranscribeRequest(BaseModel):
    file_path: str

class TTSRequest(BaseModel):
    text: str

class CalcRequest(BaseModel):
    expression: str
