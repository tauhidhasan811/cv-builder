import json

def IsValidJson(response_text):
    try:
        parsed = json.loads(response_text)
        return True, parsed
    except Exception as ex:
        return False, str(ex)