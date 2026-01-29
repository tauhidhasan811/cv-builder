
import json
import os,sys

import requests
from component.src.data.data import format_psychometric_data

def get_psychometric_data(test_id:str) -> str:

    dynamic_url = f"https://wasabigaming.vercel.app/api/v1/psychometric-attempt/{test_id}"
    api_response = requests.get(dynamic_url)
    api_response.raise_for_status()

    raw_data= api_response.json()

    formatted_data = format_psychometric_data(raw_data)
    
    return formatted_data
