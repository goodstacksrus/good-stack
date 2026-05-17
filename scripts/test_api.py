import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

model = os.getenv("LLM_MODEL", "gemini-2.5-flash")
print(f"使用モデル: {model}")
response = client.models.generate_content(
    model=model,
    contents="こんにちは、一言だけ返してください。",
)
print(response.text)
