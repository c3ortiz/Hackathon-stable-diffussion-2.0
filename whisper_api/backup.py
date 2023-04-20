from fastapi import FastAPI,UploadFile,File
from typing import List
import main
import librosa
import os
from pathlib import Path

import uvicorn
app = FastAPI()

#http://127.0.0.1:8000/
path = "temp/audio.mp3"

@app.get("/")
async def root():
    return 'funciona rey'

@app.post("/temp/")
async def upload_file(file: bytes = File(...)):
    Path(path).write_bytes(file)
    existe = os.path.exists(path)
    
    return {"existe": existe}
@app.get("/respuestas")
async def root():
    transcript = main.generate_transcript(path)
    return transcript


#if __name__ == '__main__':                                   #tenerla prendida siempre 
 #   uvicorn.run(app, host=" 127.0.0.1",port=8000 )