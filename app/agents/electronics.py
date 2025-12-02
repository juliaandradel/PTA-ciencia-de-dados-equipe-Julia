from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv
from app.knowledge import electronics_knowledge
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print("DEBUG GOOGLE_API_KEY:", api_key)

model = Gemini(
    id="models/gemini-2.5-flash",
    api_key=api_key,
)

electronics_agent = Agent(
    name="Agent_Tecnologia",
    role="Especialista técnico em Eletrônicos da O-Market",
    model=model,
    instructions=[
        "Você é a autoridade em hardware e eletrônicos.",
        "Sempre consulte sua base de conhecimento antes de responder.",
        "Cite o nome do arquivo PDF usado como fonte.",
    ],
    tools=[TavilyTools()],
    knowledge=electronics_knowledge,
    search_knowledge=True,
    markdown=True,
)


electronics_agent.print_response(
    "Liste as especificações técnicas do Eletrodomesticos Pro 300 com base no seu PDF."
)