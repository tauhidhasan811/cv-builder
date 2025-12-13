from langchain_google_genai import ChatGoogleGenerativeAI

def LoadGemini(model_name):
    model = ChatGoogleGenerativeAI(
        model_name = model_name
    )

    return model