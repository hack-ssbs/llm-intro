import requests
import json
import dotenv
import os
import base64
import pyscreenshot as ImageGrab
from datetime import datetime

im = ImageGrab.grab()

dotenv.load_dotenv()

url = "https://jamsapi.hackclub.dev/openai/chat/completions"

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def ask(img_path, prompt):
   base64_image = encode_image(img_path)
   payload = json.dumps({
      "model": "gpt-4-vision-preview",
      "stream": False,
      "messages": [
         {
            "role": "user",
            "content": [
               {
                  "type": "text",
                  "text": prompt
               },
               {
                  "type": "image_url",
                  "image_url": {
                     "url":  f"data:image/jpeg;base64,{base64_image}"
                  }
               }
            ]
         }
      ],
      "max_tokens": 400
   })
   headers = {
      'Accept': 'application/json',
      'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',
      'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)
   res = response.json()
   return res["choices"][0]["message"]['content']

while True:
    im = ImageGrab.grab()
    im.save('.screenshot.png')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('screenshot taken')
    res = ask(".screenshot.png", "categorize this screenshot. My categories are:"
                                "'coding', 'entertainment', 'academics'."
                                "Output the category only. Do not output anything else.")
    with open('log.txt', 'a') as f:
       f.write(f"{current_time}: {res}\n")