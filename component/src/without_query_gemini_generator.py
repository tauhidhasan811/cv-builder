from dotenv import load_dotenv
import google.generativeai as genai
from component.src.data import format_test_result
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.messages import HumanMessage, AIMessage
import os

# Gemini configuration 
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# Global memory registry
memory_store: dict[str, ConversationBufferMemory] = {}

def get_session_memory(session_id: str):  # Fixed typo
    if session_id not in memory_store:
        memory_store[session_id] = ConversationBufferMemory(
            return_messages=True,
            memory_key="chat_history"
        )
    return memory_store[session_id]

def get_session_history(session_id: str):
    memory = get_session_memory(session_id)
    return memory.chat_memory.messages

def add_to_memory(session_id: str, role: str, content: str):
    memory = get_session_memory(session_id)
    
    if role == 'user':
        memory.chat_memory.add_user_message(content)
    elif role == 'assistant':
        memory.chat_memory.add_ai_message(content)

def convert_to_gemini_messages(memory):

    gemini_messages = []
    
    for chat in memory:
        if isinstance(chat, HumanMessage):
            role = "user"
            content = chat.content
        elif isinstance(chat, AIMessage):
            role = "model"
            content = chat.content
        else:
            continue

        gemini_messages.append({
            "role": role,
            "parts": [content]
        })
    
    return gemini_messages

def generate_gemini_response(formatted_data, session_id: str):
    formatted_input = format_test_result(formatted_data)
    
    # Create system prompt with instructions
    prompt = (
        "Analyze the following psychometric test results data "
        f"{formatted_input}"
        "From the given test result data, provide give response this point only not single other word"
        "Provide insights on key strengths , areas for improvement, and "
        "overall feedback."
    )
    
    # Add user prompt to memory
    add_to_memory(session_id, 'user', prompt)
    
    # Get conversation history
    memory = get_session_history(session_id)
    
    # Convert to Gemini format
    gemini_messages = convert_to_gemini_messages(memory)
    
    try:
        response = model.generate_content(
            gemini_messages,
            generation_config={
                "temperature": 0.4,
                "max_output_tokens": 2080,  # Increased from 512
            }
        )
        
        assistant_response = response.text.strip() if hasattr(response, 'text') else '[empty response]'
        
        # Add response to memory
        add_to_memory(session_id, 'assistant', assistant_response)
        
        return assistant_response
        
    except Exception as e:
        print(f'Error generating gemini response: {str(e)}')
        return "Sorry, I am unable to process your request at the moment."

def clear_session_memory(session_id: str):
    if session_id in memory_store:
        del memory_store[session_id]

def get_all_sessions():
    return list(memory_store.keys())