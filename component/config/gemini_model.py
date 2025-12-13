#from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


#load_dotenv()
def LoadGemini(model_name='models/gemini-2.5-flash'):
    model = ChatGoogleGenerativeAI(
        model = model_name,
        
    )

    return model