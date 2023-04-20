import openai
import whisper
import os.path
from os import path
def generate_transcript(audio):
    model = whisper.load_model('medium')
    if path.exists(audio):
        text = model.transcribe(audio)['text']
    else:
        text ='F'
    # text = model.transcribe(audio)
    return text    
# def main():
#     while True:
#         audio = input('Audio file path:')
#         if path.exists(audio):
#             print('Valid path.')
#             transcript = generate_transcript(audio)
#             break
#         else:
#             print('File does not exists.')