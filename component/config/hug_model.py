import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()

api_key = os.environ.get('HF_TOKEN')

def HugModel(model_name="openai/whisper-large-v3", provider_name='hf-inference'):
    client = InferenceClient(
        model=model_name,
        provider=provider_name,
        api_key=api_key
    )
    return client

