"""Test OpenRouter API connection"""
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv('backend/.env')

api_key = os.getenv('OPENROUTER_API_KEY')
print(f"API Key found: {api_key[:20]}..." if api_key else "No API key")

try:
    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )
    
    response = client.chat.completions.create(
        model="google/gemini-2.0-flash-001",
        messages=[
            {"role": "user", "content": "Say 'Hello, I am working!' in one sentence."}
        ],
        max_tokens=50
    )
    
    print(f"✅ OpenRouter API is working!")
    print(f"Response: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"❌ OpenRouter API Error: {e}")
