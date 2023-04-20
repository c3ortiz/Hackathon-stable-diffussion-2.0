from flask import Flask, request, render_template
import base64
import os
import requests
import openai


# openai.api_key = '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'
# audio_file = open("static/audio/testWhisper.mp3", "rb")
# transcript = openai.Audio.transcribe("whisper-1", audio_file)

#OpenAI api key = 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

PEOPLE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/', methods =["GET", "POST"])
def index():
    transcript = ""
    # if request.method == "POST":
        # prompt = request.form.get("prompt")
        # apiKey = request.form.get("apiKey")

        # engine_id = "stable-diffusion-v1-5"
        # api_host = os.getenv('API_HOST', 'https://api.stability.ai')
        # api_key = os.getenv('STABILITY_API_KEY', apiKey)

        # if api_key is None:
        #     raise Exception("Missing Stability API key.")

        # response = requests.post(
        #     f"{api_host}/v1/generation/{engine_id}/text-to-image",
        #     headers={
        #         "Content-Type": "application/json",
        #         "Accept": "application/json",
        #         "Authorization": f"Bearer {api_key}"
        #     },
        #     json={
        #         "text_prompts": [
        #             {   
        #                 "text": prompt
        #             }
        #         ],
        #     "cfg_scale": 7,
        #     "clip_guidance_preset": "FAST_BLUE",
        #     "height": 512,
        #     "width": 512,
        #     "samples": 1,
        #     "steps": 30,
        #     },
        # )

        # if response.status_code != 200:
        #     raise Exception("Non-200 response: " + str(response.text))

        # data = response.json()

        # for i, image in enumerate(data["artifacts"]):
        #     with open(f"static/images/txt2img_{i}.png", "wb") as f:
        #         f.write(base64.b64decode(image["base64"]))
        
    response = requests.get("http://127.0.0.1:8000/respuestas",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    data = response.json()

    print(data)

        # full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'txt2img_0.png')
    # return render_template("index.html", user_image = full_filename)
    return "Funciona rey"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)