# app/agents/home_kitchen.py
import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini
from app.knowledge import home_knowledge, init_knowledge

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

model = Gemini(
    id="models/gemini-2.5-flash",
    api_key=api_key,
)

home_kitchen_agent = Agent(
    name="Agent_Casa_Conforto",
    role="Especialista em Casa e Decoração da O-Market",
    model=model,
    instructions=[
        "Você é especialista em casa e decoração da O-Market.",
        "Use apenas as informações presentes na sua base de conhecimento em PDF.",
        "Se a informação não estiver nos PDFs, diga claramente que não encontrou.",
        "Cite o nome do arquivo PDF usado como fonte.",
        "Não invente informações nem use conhecimento externo.",
    ],
    knowledge=home_knowledge,
    search_knowledge=True,
    markdown=True,
)

def main():
    init_knowledge(load_electronics=False, load_home=True)
    home_kitchen_agent.print_response(
        "Liste as especificações técnicas do Alimentos Plus 100 com base no seu PDF."
    )

if __name__ == "__main__":
    main()
