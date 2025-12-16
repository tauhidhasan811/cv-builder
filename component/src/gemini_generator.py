
from dotenv import load_dotenv
import google.generativeai as genai
from component.src.data import formatted_data
from langchain_classic.memory import ConversationBufferMemory
# from langchain_classic.chains import LLMChain
from langchain_core.messages import HumanMessage, AIMessage


import os
# gemini configuration 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

#global memory registry
memory_store = dict[str, ConversationBufferMemory] = {}

def get_sesion_memory(session_id:str):
    if session_id not in memory_store:
        memory_store[session_id] = ConversationBufferMemory(
            return_messages=True,
            memory_key="chat_history"
        )

    return memory_store[session_id]

def get_session_history(session_id:str):
    memory = get_sesion_memory(session_id)
    return memory.chat_memory.messages

def add_to_memory(session_id:str, role:str, content:str):
    memory = get_sesion_memory(session_id)

    if role == 'user':
        memory.chat_memory.add_user_message(content)
    elif role == 'assistant':
        memory.chat_memory.add_ai_message(content)
 

def convert_to_gemini_messages(system_prompt, memory):

    gemini_messgaes = []
    gemini_messgaes.append({
        "role":"user",
        "parts": [system_prompt["content"]]
    })

    for chat in memory:
        if isinstance(chat, HumanMessage):
            role = 'user'
            content = chat.content
        elif isinstance(chat, AIMessage):
            role = 'model'
            content = chat.content
        else:
            continue
        gemini_messgaes.append({
            'role': role,
            'parts': [content]
        })     
    return gemini_messgaes

def generate_gemini_response(query, formatted_data, session_id:str):
    system_prompt = {
        "role": "system",
        "content": (
            f"You are a helpful assistant that provides accurate and precise information "
            f"based on the psychometric test result data {formatted_data}. "
            f"From the given test result data, provide give response this point only not single other word like here in analysis result or other words: "
            f"1) Recomanded skills based on the psychometric test result."
            f"2) Key strengths (3 points), "
            f"3) Areas for improvement (3 points), "
            f"4) Overall feedback (short)."
        )
    }
    
    add_to_memory(session_id, 'user', query)
    memory = get_session_history(session_id)
    gemini_messages = convert_to_gemini_messages(system_prompt, session_id)

    try:
        response  = model.generate_content(
            gemini_messages,
            generation_config={
                "temperature": 0.4,
                "max_output_tokens":256,
                "top_p":0.8,
                "top_k":40
            }
        )
        assistant_response = response.text.strip() if hasattr(response, 'text') else '[empty response]'
        add_to_memory(session_id, 'assistant', assistant_response)
        return assistant_response
    except Exception as e:
        print('Error generating gemini response:', str(e))
        return "Sorry, I am unable to process your request at the moment."


def clear_session_memory(session_id:str):
    if session_id in memory_store:
        del memory_store[session_id]

def get_all_sessions():
    return list(memory_store.keys())








