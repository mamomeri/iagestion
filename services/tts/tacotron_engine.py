# ruta: services/tts/tacotron_engine.py

import os
import torch
import soundfile as sf
import textwrap
import time
import simpleaudio as sa
from datetime import datetime
from speechbrain.inference.TTS import Tacotron2
from speechbrain.inference.vocoders import HIFIGAN
from config.settings import get_settings

# Inicializa modelos Tacotron2 + HifiGAN
tacotron = Tacotron2.from_hparams(
    source="speechbrain/tts-tacotron2-ljspeech", 
    savedir="tmp_tacotron2"
)
hifigan = HIFIGAN.from_hparams(
    source="speechbrain/tts-hifigan-ljspeech", 
    savedir="tmp_hifigan"
)

settings = get_settings()

def dividir_texto(texto, max_chars=20):
    return textwrap.wrap(texto, width=max_chars, break_long_words=True)

def synthesize_text(text: str, language: str = "en", reproducir: bool = True):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = os.path.join("Data", "audio_output", f"tts_tacotron_{timestamp}")
    os.makedirs(folder, exist_ok=True)

    fragmentos = dividir_texto(text)
    archivos = []

    for i, frag in enumerate(fragmentos):
        mel_output, mel_len, align = tacotron.encode_text([frag])
        wav = hifigan.decode_batch(mel_output).squeeze(1).cpu().numpy()

        fname = os.path.join(folder, f"{i+1:05}.wav")
        sf.write(fname, wav, samplerate=22050)
        archivos.append(fname)

        if reproducir:
            wave_obj = sa.WaveObject.from_wave_file(fname)
            play = wave_obj.play(); play.wait_done(); time.sleep(0.1)

    return folder
