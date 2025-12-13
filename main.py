from fastapi import FastAPI, Form
from component.services.cv_prompt import CVPrompt

#prompt = CVPrompt(user_text="Nothing to say", user_data="Name: Tauhid Hasan\nUniversity: AIUB")

#print(prompt)

app = FastAPI()

@app.post('/api/check-prompt/')
def check_prompt(user_text:str = Form(),
                 user_data = Form()):
    try:
        prompt = CVPrompt(user_text=user_text,
                          user_data=user_data)
        response = {
            'status': True,
            'statuscode': 200,
            'text': prompt
        }

        print(response)

        return response
    except Exception as ex:
        response = {
            'status': False,
            'statuscode': 500,
            'text': str(ex)
        }