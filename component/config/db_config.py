import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

def GetDBConnection():
    uri = os.environ.get('MONGO_URI')
    client = MongoClient(uri)
    print(client.admin.command('ping'))
    return client['cv_builder']