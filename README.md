# Mini-Project: Smart Time-Tracking with Vision Language Models

This repo contains a CS Club mini-project project that introduces the use of large language models and vision language models.

Specifically, `main.py` contains a program that periodically fetches a screenshot of your computer,
uses a vision language model(gpt4-v in this case) to categorize what you're working on into categories,
and dump it into a log. 

## How to run this

First, create a `.env` file in this folder with the following contents:
```
OPENAI_API_KEY=<your openai api key>
OPENAI_API_BASE=<your openai api base> // OPTIONAL
```

Then, run this in your shell/terminal/command line:
```shell
pip install -r requirements.txt
python main.py
```

## Possible Areas of Improvement
The mini-project is very rudimentary! ALl sorts of improvements are possible and welcome!
Here are some ideas on how to get started

- Add support for local vision language models
- Run the VLLM labeling process in a separate thread
- Introduce more categories, perhaps even dynamic categories
- Add analytics mechanisms for our log / improve our logging mechanism
- Add Graphical User Interface