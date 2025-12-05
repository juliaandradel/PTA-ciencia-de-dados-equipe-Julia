import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.google import Gemini

from app.knowledge import electronics_knowledge, init_knowledge

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

model = Gemini(
    id="models/gemini-2.5-flash",
    api_key=api_key,
)

electronics_agent = Agent(
    name="Agent_Tecnologia",
    role="Especialista técnico em Eletrônicos da O-Market",
    model=model,
    instructions=[
        "Você é especialista em eletrônicos da O-Market.",
        "Use apenas as informações presentes na sua base de conhecimento em PDF.",
        "Se a informação não estiver nos PDFs, diga claramente que não encontrou.",
        "Cite o nome do arquivo PDF usado como fonte.",
        "Não invente informações nem use conhecimento externo.",
    ],
    knowledge=electronics_knowledge,
    search_knowledge=True,
    markdown=True,
)

def main():
    init_knowledge(load_electronics=True, load_home=False)

    electronics_agent.print_response(
        "Liste as especificações técnicas do Eletrodomesticos Premium 400 com base no seu PDF."
    )

if __name__ == "__main__":
    main()
