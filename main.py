from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from component.config.gemini_model import LoadGemini
from component.services.db_service import InsertService
from component.services.coverletter_prompt import CLPrompt
from component.services.cv_prompt import CVPrompt, DescPrompt, SummPrompt
from component.src.gemini_without_langchain import generate_gemini_response

#prompt = CVPrompt(user_text="Nothing to say", user_data="Name: Tauhid Hasan\nUniversity: AIUB")

#print(prompt)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


load_dotenv()

model = LoadGemini()


class CheckRequest(BaseModel):
    session_id: str
    user_payload: dict


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

@app.post('/api/gen-cover-letter/')
async def generate_cl(job_desc = Form(),
                      user_data = Form(), 
                      additional_note = Form(None)):
    try:
        prompt = CLPrompt(user_data=user_data, job_desc=job_desc, additional_note=additional_note)

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
        return message


@app.post('/api/enhance-desc/')
def enhance_desc(job_information = Form(),
             job_summary = Form()):
    try:
        prompt = DescPrompt(job_information= job_information, 
                            job_summary=job_summary)
        
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


@app.post("/api/anlz-psychometric/")
async def check(data: CheckRequest):

    try:
        response = generate_gemini_response(data.user_payload, data.session_id)

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