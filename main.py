import os
import time
import json
import asyncio
import tempfile
import requests
from dotenv import load_dotenv
from pydantic import BaseModel
from component.core.clear_data import CleanData
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, File, UploadFile
from component.config.audio_model import OpenAIAudio
from component.src.data.data import format_psychometric_data
from component.src.openai_generator import generate_openai_response, clear_session
from component.config.openai_model import LoadGPT
from component.core.video_to_audio import ExtractAudio
#from component.config.gemini_model import LoadGemini
#from component.services.db_service import InsertService
#from component.core.check_valid_json import IsValidJson
#from component.core.video_to_audio import ExtractAudio
from component.services.prompt_coverletter import CLPrompt
#from component.services.prompt_mock_test import MockQuesPrompt, MockAnsPrompt
from component.services.prompt_mock_test import MokeEvaluatePrompt
from component.services.prompt_cv_maker import DescPrompt, SummPrompt

from component.core.job_scrape import scrape_all
import component.parameters as hparams




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


load_dotenv()

#model = LoadGemini()
model = LoadGPT()
audio_model = OpenAIAudio()


class CheckRequest(BaseModel):
    test_id: str



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

        test_id = data.test_id
        dynamic_api_url = f"https://wasabigaming.vercel.app/api/v1/psychometric-test/{test_id}"
        api_response = requests.get(dynamic_api_url, timeout=10)
        api_response.raise_for_status()
        raw_test_data = api_response.json()

        # Format data for OpenAI
        formatted_data = format_psychometric_data(raw_test_data)
        session_id = data.test_id  # Use test_id as session

        # Generate concise psychometric insights
        response = generate_openai_response(
            user_message=formatted_data["text"],
            session_id=session_id
        )

        clear_session(session_id)

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



@app.post("/api/mock-interview/")
async def check_mock_answer(question = Form(),
                            answer = Form(),
                            segment = Form(),
                            video: UploadFile = File()):
    try:
        with tempfile.TemporaryDirectory() as dir:
            f_name = video.filename
            a_f_name = f_name.split('.')[0] +'.mp3'
            path = os.path.join(dir, f_name)

            with open(path, 'wb') as file:
                file.write(await video.read())
            print(path)

            aud_pth = os.path.join(dir, a_f_name)
            response = ExtractAudio(path, aud_pth)
            answer_text = await asyncio.to_thread(audio_model.ConvertToText, aud_pth)

        
            #time.sleep(90)
        
        prompt = MokeEvaluatePrompt(segment=segment, question=question,
                                    answer=answer_text)
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


@app.post("/api/find-jobs/")
async def find_jobs(job_title= Form(),
                    location = Form()):
    try:
        BASE_URL = hparams.hparams["BASE_URL"]
        HEADERS = hparams.hparams["HEADERS"]

        START_URL = hparams.build_search_url(search_term=job_title, 
                                             location=location)

    
        jobs = scrape_all(BASE_URL, START_URL, HEADERS)
        print('-' * 100)
        print(f"Total jobs scraped: {len(jobs)}")
        print('-' * 100)


        response = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'text': jobs
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


