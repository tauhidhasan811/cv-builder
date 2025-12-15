from dotenv import load_dotenv
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from component.config.gemini_model import LoadGemini
from component.services.db_service import InsertService
from component.services.cv_prompt import CVPrompt, DescPrompt, SummPrompt

#prompt = CVPrompt(user_text="Nothing to say", user_data="Name: Tauhid Hasan\nUniversity: AIUB")

#print(prompt)

app = FastAPI()
load_dotenv()

model = LoadGemini()

"""
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
        return response
    """

@app.post('/api/enhance-desc/')
def enhance_desc(job_information = Form(),
             job_summary = Form()):
    try:
        prompt = DescPrompt(job_information= job_information, job_summary=job_summary)
        
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


@app.post('/api/enhance-summ/')
async def enhance_summary(user_summary = Form(),
                          user_data = Form()):
    try:
        prompt = SummPrompt(user_summary=user_summary, user_data=user_data)
        print(prompt)
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
        message = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'statuscode': 500,
                'text': str(ex)
            }
        )
        return message

"""@app.post('/api/gen-cv/')
async def generate_cv(additional_note, user_data):
    try:
        prompt = CVPrompt(additional_note, user_data)

        response = model.invoke(prompt).content

        message = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'statuscode': 200,
                'text': response
            }
        )
        return message
    except Exception as ex:
        message = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'statuscode': 500,
                'text': str(ex)
            }
        )
        return message"""