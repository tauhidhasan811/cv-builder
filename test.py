from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
"""
client = OpenAI()
"""

"""
audio_file = open("audio.mp3", "rb")

stream = client.audio.transcriptions.create(
  model="gpt-4o-mini-transcribe", 
  file=audio_file, 
  response_format="text",
  stream=True
)

for event in stream:
  print(event)
"""
"""

model = OpenAI().models

print(model)"""

"""from component.config.audio_model import OpenAIAudio

model = OpenAIAudio()
audio_path = "audio.mp3"

text = model.ConvertToText(audio_path=audio_path)

print(text)"""

"""from component.services.mocktest_prompt import MockTestPrompt

prompt = MockTestPrompt(domain_name="Law", topic_name = 'creminal', 
                        num_of_question="10", def_level='hard')
print(prompt)"""

import os
import tempfile


