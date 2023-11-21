import requests
import json
import dotenv
import os
import base64
import pyscreenshot as ImageGrab
from datetime import datetime
from io import BytesIO

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE") or "https://api.openai.com/v1"

def encode_im(im):
    virtual_file = BytesIO()
    im.save(virtual_file, 'PNG')
    return base64.b64encode(virtual_file.getvalue()).decode('utf-8')

def ask(im, prompt):
   base64_image = encode_im(im)
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

   response = requests.request("POST", f"{OPENAI_API_BASE}chat/completions", headers=headers, data=payload)
   res = response.json()
   cat = res["choices"][0]["message"]['content']
   print(f"category: {cat}")
   return cat

while True:
    im = ImageGrab.grab()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('screenshot taken')
    res = ask(im, "categorize this screenshot. My categories are:"
                                "'coding', 'entertainment', 'academics'."
                                "Output the category only. Do not output anything else.")
    with open('log.txt', 'a') as f:
       f.write(f"{current_time}: {res}\n")