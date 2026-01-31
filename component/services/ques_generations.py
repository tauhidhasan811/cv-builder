from component.config.openai_model import LoadGPT
from component.services.written_test import generate_question_prompt
import json
from component.services.written_presentation import written_presentation_ques_generator
from component.services.in_tray_email import in_tray_email_ques_generator
from component.services.case_law_summary import generate_case_law_summary_question
model = LoadGPT(temp=1)

print('=' * 100)
print(model.temperature)
print('=' * 100)

def get_generated_questions():
    prompt = generate_question_prompt()
    response = model.invoke(prompt)
    return json.loads(response.content)

def get_presentation_questions():
    prompt = written_presentation_ques_generator()
    response = model.invoke(prompt)
    return json.loads(response.content)


def generate_in_tray_email_task():
    prompt= in_tray_email_ques_generator()
    response = model.invoke(prompt)
    return json.loads(response.content)


def generate_case_law_summary_questions():
    prompt = generate_case_law_summary_question()
    response = model.invoke(prompt)
    return json.loads(response.content)