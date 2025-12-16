# from without_query_gemini_generator import generate_gemini_response
from gemini_without_langchain import generate_gemini_response
from dotenv import load_dotenv
from data import formatted_data 
load_dotenv()

def main():
    print("Generating psychometric test analysis using Gemini...\n")


    #session_id = formatted_data['session_id']
    session_id = input('Enter session data: ')
    user_payload = formatted_data

    response = generate_gemini_response(user_payload, session_id)
   
    print("=" * 80)
    print("GEMINI RESPONSE:")
    print("=" * 80)
    print(response)
    print("=" * 80)

if __name__ == "__main__":
    main()

