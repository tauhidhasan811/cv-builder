from dotenv import load_dotenv
import google.generativeai as genai
from component.src.data import format_test_result
from typing import Dict, List
import os

# Gemini configuration 
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# Simple memory structure without LangChain
memory_store ={}

def get_session_memory(session_id: str) -> List[Dict[str, str]]:
    """Get or create conversation history for a session"""
    if session_id not in memory_store:
        memory_store[session_id] = []
    return memory_store[session_id]

def add_to_memory(session_id: str, role: str, content: str):
    """Add a message to session memory"""
    memory = get_session_memory(session_id)
    memory.append({
        "role": "user" if role == "user" else "model",
        "content": content
    })

def convert_to_gemini_messages(memory: List[Dict[str, str]]) -> List[Dict]:
    """Convert memory to Gemini message format"""
    return [
        {
            "role": msg["role"],
            "parts": [msg["content"]]
        }
        for msg in memory
    ]

def generate_gemini_response(formatted_data, session_id: str):
    formatted_input = format_test_result(formatted_data)
    
    # Create prompt with instructions
    prompt = (
        "Analyze the following psychometric test results"
         f"Test data:\n{formatted_input}"
        " and generate provide give response this point only not single other word like here in analysis result or other words and reponse will be in those four points like point nake : text:\n"
        "1) Recomanded skills eatch skill name within 2 word based on the psychometric test result."
        "2) Key strengths in 3 words\n"
        "3) Areas for improvement in 3 words\n"
        "4) A concise overall feedback within 1-2 line.\n\n"
        
    )
    
    # Add user prompt to memory
    add_to_memory(session_id, 'user', prompt)
    
    # Get conversation history
    memory = get_session_memory(session_id)
    
    # Convert to Gemini format
    gemini_messages = convert_to_gemini_messages(memory)
    
    try:
        response = model.generate_content(
            gemini_messages,
            generation_config={
                "temperature": 0.4,
                "max_output_tokens": 2048,
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
    """Clear memory for a specific session"""
    if session_id in memory_store:
        del memory_store[session_id]

def get_all_sessions() -> List[str]:
    """Get all active session IDs"""
    return list(memory_store.keys())

def get_session_history(session_id: str) -> List[Dict[str, str]]:
    """Get full conversation history for a session"""
    return get_session_memory(session_id)