from agno.agent import Agent
from agno.models.google import Gemini
from app.knowledge import electronics_knowledge # Importamos do arquivo novo

electronics_agent = Agent(
    name="Agent_Tecnologia",
    role="Especialista técnico em Eletrônicos da O-Market",
    model=Gemini(id="gemini-1.5-flash-002"),
    instructions=[
        "Você é a autoridade em hardware e eletrônicos.",
        "Sempre consulte sua base de conhecimento antes de responder.",
        "Cite o nome do arquivo PDF usado como fonte."
    ],
    knowledge=electronics_knowledge, # Usa o objeto importado
    search_knowledge=True,
    markdown=True,
    show_tool_calls=True
)