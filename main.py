from time import sleep
from click import File
from flask import Flask, redirect, request, render_template, session, url_for
from PIL import Image
import base64
import os
import requests
import openai

PEOPLE_FOLDER = os.path.join('static', 'images')
AUDIO_FOLDER = os.path.join('static', 'audio')

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.secret_key = b'_5#zxcfy2L"esdf\n\xec]/'

@app.route('/', methods =["GET", "POST"])
def index():

    if request.method == "POST":

        if 1 == 1:
            return redirect("/loading", code=302)
            

        sleep(5)
        
        # OPENAI_API_KEY = request.form.get("openaiapikey")
        # STABLEDIFF_API_KEY = request.form.get("stablediffapikey")
        # PROJECT_NAME = request.form.get("projectname")
        # AUDIO_FILE = request.files['audioFile']

        # AUDIO_FILE.save(os.path.join(AUDIO_FOLDER, "fileFromFrontend.mp3"))

        # # API WHISPER

        # openai.api_key = OPENAI_API_KEY
        # audio_file = open(os.path.join(AUDIO_FOLDER, "fileFromFrontend.mp3"), "rb")
        # transcript = openai.Audio.transcribe("whisper-1", audio_file)

        # promptToChatGPT = transcript.text

        # # API CHATGPT

        # input_prompt = "Summarize:" + promptToChatGPT

        # completionSummary = openai.ChatCompletion.create(
        #     model = 'gpt-3.5-turbo',
        #     messages = [
        #         {'role': 'user', 'content': input_prompt}
        #     ],
        #     temperature = 0,
        #     max_tokens = 200
        # )

        # summary = completionSummary['choices'][0]['message']['content']

        # completionPrompts = openai.ChatCompletion.create(
        #     model = 'gpt-3.5-turbo',
        #     messages = [
        #         {'role': 'user', 'content': "Visual description of key concepts of: " + summary}
        #     ],
        #     temperature = 0,
        #     max_tokens = 200
        # )

        # promptsToStableDiffusion = completionPrompts['choices'][0]['message']['content'].split(". ")

        # completionQuestions = openai.ChatCompletion.create(
        #     model = 'gpt-3.5-turbo',
        #     messages = [
        #         {'role': 'user', 'content': "Questions of key concepts of: " + summary}
        #     ],
        #     temperature = 0,
        #     max_tokens = 200
        # )

        # questions = completionQuestions['choices'][0]['message']['content']

        # # API STABLE DIFFUSSION

        # engine_id = "stable-diffusion-v1-5"
        # api_host = 'https://api.stability.ai'
        # api_key = STABLEDIFF_API_KEY

        # if api_key is None:
        #    raise Exception("Missing Stability API key.")

        # for j in range(0, len(promptsToStableDiffusion)):
        #     response = requests.post(
        #         f"{api_host}/v1/generation/{engine_id}/text-to-image",
        #         headers={
        #             "Content-Type": "application/json",
        #             "Accept": "application/json",
        #             "Authorization": f"Bearer {api_key}"
        #         },
        #         json={
        #             "text_prompts": [
        #                 {   
        #                     "text": promptsToStableDiffusion[j]
        #                 }
        #             ],
        #         "cfg_scale": 7,
        #         "clip_guidance_preset": "FAST_BLUE",
        #         "height": 250,
        #         "width": 250,
        #         "samples": 1,
        #         "steps": 30,
        #         },
        #     )

        #     if response.status_code != 200:
        #         raise Exception("Non-200 response: " + str(response.text))

        #     data = response.json()

        #     for i, image in enumerate(data["artifacts"]):
        #         with open(f"static/images/txt2img_{j}.png", "wb") as f:
        #             f.write(base64.b64decode(image["base64"]))

        # image_urls = []

        # for i in range(0, len(promptsToStableDiffusion)):
        #     image_urls.append(os.path.join(PEOPLE_FOLDER, f'txt2img_{i}.png'))

        # session['summary'] = summary
        # session['questions'] = questions
        # session['images'] = image_urls
        # session['projectName'] = PROJECT_NAME

        return redirect("/response", code=302)
    
    return render_template('index.html')
        

@app.route('/loading', methods =["GET", "POST"])
def loading():
    return render_template('loading.html')

@app.route('/response', methods =["GET", "POST"])
def response():
    summary = session['summary']
    questions = session['questions']
    image_urls = session['images']
    projectName = session['projectName']

    return render_template('response.html', url = image_urls, summary = summary, questions = questions, projectName = projectName)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)