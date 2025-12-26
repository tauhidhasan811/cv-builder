from openai import OpenAI

class OpenAIAudion:
    def __init__(self, model_name = "whisper-1"):
        self.client = OpenAI()