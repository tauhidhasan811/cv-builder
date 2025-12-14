from datetime import datetime
from model.insert import insert_one

def InsertService(text:str, cl_name, chat_id, query_id = None):
    date = datetime.now()

    if query_id ==None:
        data = {
            'text': text,
            'date': date,
            'chat_id': chat_id
        }
    else :
        data = {
            'text': text,
            'date': date,
            'chat_id': chat_id
        }
    id = insert_one(data=data, cl_name=cl_name)
    return id