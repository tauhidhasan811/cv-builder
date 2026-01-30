
import json
# from component.config.openai_model import LoadGPT

import requests
from component.src.data.data import format_psychometric_data
def get_psycho_data(test_id: str):
    try:
        dynamic_url = f"https://wasabigaming.vercel.app/api/v1/psychometric-attempt/{test_id}"
        # print(f"Fetching from URL: {dynamic_url}")
        
        api_response = requests.get(dynamic_url)
        api_response.raise_for_status()
        
        raw_data = api_response.json()
        # print(f"Raw API response: {raw_data}")
        
        # Check if response is successful
        if not raw_data.get('success'):
            raise ValueError(f"API returned error: {raw_data.get('message')}")
        
        formatted_data = format_psychometric_data(raw_data)
        return formatted_data
        
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        raise
    except Exception as e:
        print(f"Error formatting data: {e}")
        raise
