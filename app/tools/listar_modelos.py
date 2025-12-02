from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY não encontrada. Defina no .env ou no ambiente.")
client = genai.Client(api_key=api_key)

print("Modelos disponíveis para generateContent:\n")
for model in client.models.list():
    supported = getattr(model, "supported_actions", [])
    if "generateContent" in supported:
        print(model.name)
