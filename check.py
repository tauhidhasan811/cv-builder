from dotenv import load_dotenv
from component.config.gemini_model import LoadGemini

load_dotenv()

model = LoadGemini()

res = model.invoke('hi').content
print(res)