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

"""import json

def is_valid_json(response_text):
    try:
        parsed = json.loads(response_text)
        return True, parsed
    except json.JSONDecodeError:
        return False, None

# Example usage:
response = '{"Result": "CORRECT", "Score": "90%", "Reason": "Answer is mostly correct"}'

valid, data = is_valid_json(response)
if valid:
    print("Valid JSON:", data)
else:
    print("Invalid JSON")
"""

import re

text = r'''
\[{\"question\": \"Explain the difference between word embeddings and one-hot encoding.\"}\]
```json
\bash
'''

# Step 1: Remove all literal backslashes
cleaned = text.replace("\\", "")

# Step 2: Remove backticks (` or ``` )
cleaned = re.sub(r"`{1,3}", "", cleaned)

# Step 3: Remove code language keywords (json, bash, python, etc.)
cleaned = re.sub(r'\b(json|bash|python)\b', '', cleaned, flags=re.IGNORECASE)

# Step 4: Remove newlines and extra spaces
cleaned = re.sub(r'\s+', ' ', cleaned).strip()

print(cleaned)
