from dotenv import load_dotenv
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from component.services.cv_prompt import CVPrompt
from component.config.gemini_model import LoadGemini

#prompt = CVPrompt(user_text="Nothing to say", user_data="Name: Tauhid Hasan\nUniversity: AIUB")

#print(prompt)

app = FastAPI()
load_dotenv()

@app.post('/api/check-prompt/')
def check_prompt(user_text:str = Form(),
                 user_data = Form()):
    try:
        prompt = CVPrompt(user_text=user_text,
                          user_data=user_data)
        response = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'statuscode': 200,
                'text': prompt
            }
        )
        print(response)
        return response
    
    except Exception as ex:
        response = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'statuscode': 500,
                'text': str(ex)
            }
        )
@app.post('/api/gen-descrption/')
def gen_desc(user_text = Form(),
             user_data = Form()):
    try:
        model = LoadGemini()
        prompt = CVPrompt(user_text=user_text, 
                          user_data=user_data)
        response = model.invoke(prompt)

        message = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'statuscode': 200,
                'text': response.content
            }
        )
        return message
    except Exception as ex:
        response = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'statuscode': 500,
                'text': str(ex)
            }
        )
        return response