from datetime import datetime
from dotenv import load_dotenv
from component.config.gemini_model import LoadGemini
from component.config.db_config import GetDBConnection
from component.services.db_service import InsertService
from component.config.gemini_model import LoadGemini
from component.services.db_service import InsertService
from component.services.prompt_cv_maker import CVPrompt, DescPrompt, SummPrompt

#prompt = CVPrompt(user_text="Nothing to say", user_data="Name: Tauhid Hasan\nUniversity: AIUB")

#print(prompt)


load_dotenv()

model = LoadGemini()
load_dotenv()

#GetDBConnection()

#print(datetime.now())

#id = InsertService(text = 'test_text', cl_name='user_query', chat_id=1)
#print(id)
"""
model = LoadGemini()

res = model.invoke('hi').content
print(res)"""

prompt = SummPrompt(user_summary='user_summary', user_data='user_data')
print(prompt)
   
response = model.invoke(prompt)
print(response)