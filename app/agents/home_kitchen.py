from agno.agent import Agent
from agno.models.google import Gemini
from app.knowledge import home_knowledge

home_kitchen_agent = Agent(
    name="Agent_Casa_Conforto",
    role="Especialista em Casa e Decoração da O-Market",
    model=Gemini(id="gemini-1.5-flash-002"),
    instructions=[
        "Foque em materiais, dimensões e design.",
        "Sempre consulte sua base de conhecimento.",
        "Cite o nome do arquivo PDF usado como fonte."
    ],
    knowledge=home_knowledge,
    search_knowledge=True,
    markdown=True,
    show_tool_calls=True
)