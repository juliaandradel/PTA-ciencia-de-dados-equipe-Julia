from agno.agent import Agent
from agno.models.google import Gemini
from app.knowledge import electronics_knowledge

electronics_agent = Agent(
    name="Agent_Tecnologia",
    role="Especialista técnico em Eletrônicos da O-Market",
    # AQUI ESTÁ A CORREÇÃO MÁGICA 👇
    model=Gemini(id="models/gemini-1.5-flash"),
    instructions=[
        "Você é a autoridade em hardware e eletrônicos.",
        "Sempre consulte sua base de conhecimento antes de responder.",
        "Cite o nome do arquivo PDF usado como fonte."
    ],
    knowledge=electronics_knowledge,
    search_knowledge=True,
    markdown=True,
    show_tool_calls=True
)