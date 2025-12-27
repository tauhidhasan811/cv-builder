import os
import time
import json
import asyncio
import tempfile
from dotenv import load_dotenv
from pydantic import BaseModel
from component.core.clear_data import CleanData
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, File, UploadFile
from component.config.audio_model import OpenAIAudio
from component.config.openai_model import LoadGPT
from component.config.gemini_model import LoadGemini
from component.services.db_service import InsertService
from component.core.check_valid_json import IsValidJson
from component.services.prompt_coverletter import CLPrompt
from component.services.prompt_mock_test import MockQuesPrompt, MockAnsPrompt
from component.services.prompt_cv_maker import CVPrompt, DescPrompt, SummPrompt
from component.src.gemini_without_langchain import generate_gemini_response

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
#model = LoadGPT()
audio_model = OpenAIAudio()


class CheckRequest(BaseModel):
    session_id: str
    user_payload: dict



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


@app.post("/api/gen-mock-question/")
async def gen_mock_question(domain_name = Form(),
                            topic_name = Form(),
                            num_of_question = Form(),
                            def_level = Form()):
    try:
        prompt = MockQuesPrompt(domain_name=domain_name, topic_name = topic_name, 
                            num_of_question=num_of_question, def_level=def_level)
        
        questions = model.invoke(prompt).content

        questions = CleanData(questions)

        message = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'text': questions
            })
        return message
    except Exception as ex:

        message = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'text': str(ex)
            })
        
        return message


@app.post("/api/speech-text/")
async def conver_speech_text(audio:UploadFile = File()):
    try:

        f_name = audio.filename
        #dir = tempfile.mkdtemp()
        with tempfile.TemporaryDirectory() as dir: 
            audio_path = os.path.join(dir, f_name)

            with open(audio_path, 'wb') as file:
                file.write(await audio.read())
                #file.write(audio.read())
            print(audio_path)
            
            #text = audio_model.ConvertToText(audio_path=audio_path)
            text = await asyncio.to_thread(audio_model.ConvertToText, audio_path)
            #time.sleep(30)
        response =JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'text': text
            })
        
        return response
    except Exception as ex:

        response =JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'text': str(ex)
            }
        )
        return response


@app.post("/api/check-answer/")
async def check_mock_answer(domain_name = Form(),
                            topic_name = Form(),
                            question = Form(),
                            answer = Form()):
    try:
        prompt = MockAnsPrompt(domain_name=domain_name,
                            topic_name=topic_name,
                            question=question,
                            answer=answer)
        

        message = model.invoke(prompt).content
        message = CleanData(message)

        response = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'text': message
            }
        )
        return response
    except Exception as ex:
        response = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'text': str(ex)
            }
        )
        return response



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

