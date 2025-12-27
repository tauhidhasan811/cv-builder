
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Simple in-memory conversation storage
conversations = {}

SYSTEM_PROMPT = """Rewrite psychometric insights into concise natural language:
- Key strengths (~3 words)
- Areas for improvement (~3 words)
- Overall feedback (1-2 lines)
Be direct and concise."""


def generate_openai_response(user_message: str, session_id: str):

    # Initialize conversation if new sessio
    if session_id not in conversations:
        conversations[session_id] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
    
    # Add user message
    conversations[session_id].append({
        "role": "user",
        "content": user_message
    })
    
    try:
        # Call OpenAI API (correct method)
        response = client.chat.completions.create(
            model="gpt-5-mini",  # Fixed model name
            messages=conversations[session_id]
            # max_tokens=256,
            # temperature=0.7
        )
        
        
        assistant_message = response.choices[0].message.content
        
        conversations[session_id].append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
        
    except Exception as e:
        print(f"OpenAI error: {e}")
        return "Sorry, I am unable to process your request."


def clear_session(session_id: str):
    """Clear conversation history for a session"""
    conversations.pop(session_id, None)


def get_session_history(session_id: str):
    """Get conversation history for a session"""
    return conversations.get(session_id, [])


def get_all_sessions():
    """Get all active session IDs"""
    return list(conversations.keys())


