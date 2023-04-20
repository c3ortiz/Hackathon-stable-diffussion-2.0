from flask import Flask, request, render_template
from PIL import Image
import base64
import os
import requests
import openai

PEOPLE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/', methods =["GET", "POST"])
def index():
    # if request.method == "POST":

        # OPENAI_API_KEY = request.form.get("openaiapikey")
        # STABLEDIFF_API_KEY = request.form.get("stablediffapikey")

        # API WHISPER

        # response = requests.get("http://127.0.0.1:8000/respuestas",
        # headers={
        #      "Content-Type": "application/json",
        #      "Accept": "application/json",
        #  })

        # data = response.json()

        # API CHATGPT

        # openai.api_key = OPENAI_API_KEY
        # input_prompt = "Summarize:" + data

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
        #         {'role': 'user', 'content': "Questions of key concepts of: "+ summary}
        #     ],
        #     temperature = 0,
        #     max_tokens = 200
        # )

        # questions = completionQuestions['choices'][0]['message']['content']

        # API STABLE DIFFUSSION

        # engine_id = "stable-diffusion-v1-5"
        # api_host = os.getenv('API_HOST', 'https://api.stability.ai')
        # api_key = os.getenv('STABILITY_API_KEY', STABLEDIFF_API_KEY)

        # if api_key is None:
        #    raise Exception("Missing Stability API key.")

        # for i in range(0, len(promptsToStableDiffusion)):
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
        #                     "text": promptsToStableDiffusion[i]
        #                 }
        #             ],
        #         "cfg_scale": 7,
        #         "clip_guidance_preset": "FAST_BLUE",
        #         "height": 512,
        #         "width": 512,
        #         "samples": 1,
        #         "steps": 30,
        #         },
        #     )

        #     if response.status_code != 200:
        #         raise Exception("Non-200 response: " + str(response.text))

        #     data = response.json()

        #     for i, image in enumerate(data["artifacts"]):
        #         with open(f"static/images/txt2img_{i}.png", "wb") as f:
        #             f.write(base64.b64decode(image["base64"]))

        image_urls = ['static/images/txt2img_0.png', 'static/images/txt2img_1.jpeg', 'static/images/txt2img_2.jpeg']
        # singleImage = Image.open("static/images/txt2img_0.png")

        # for i in range(0, len(promptsToStableDiffusion)):
            # listOfImages[i] = os.path.join(PEOPLE_FOLDER, f'txt2img_{i}.png')

        return render_template('index.html', image_urls=image_urls)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)