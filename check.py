from datetime import datetime
from dotenv import load_dotenv
from component.config.gemini_model import LoadGemini
from component.config.db_config import GetDBConnection
from component.services.db_service import InsertService

load_dotenv()

GetDBConnection()

print(datetime.now())

id = InsertService(text = 'test_text', cl_name='user_query', chat_id=1)
print(id)
"""
model = LoadGemini()

res = model.invoke('hi').content
print(res)"""