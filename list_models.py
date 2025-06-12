import openai
from dotenv import load_dotenv
import os

print("Starting script...")  # Test

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("Loaded API key:", api_key[:8] + "..." if api_key else "None")

client = openai.OpenAI(api_key=api_key)

models = client.models.list()

print("Available models:")
for model in models.data:
    print("-", model.id)