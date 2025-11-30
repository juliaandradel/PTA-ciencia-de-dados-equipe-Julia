from agno.agent import Agent
from agno.models.google import Gemini
from app.knowledge import electronics_knowledge # Importamos do arquivo novo
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv
load_dotenv()

electronics_agent = Agent(
    name="Agent_Tecnologia",
    role="Especialista técnico em Eletrônicos da O-Market",
    model=Gemini(id="models/gemini-2.5-flash"),
    instructions=[
        "Você é a autoridade em hardware e eletrônicos.",
        "Sempre consulte sua base de conhecimento antes de responder.",
        "Cite o nome do arquivo PDF usado como fonte."
    ],
    tools = [TavilyTools()],
    knowledge=electronics_knowledge, # Usa o objeto importado
    search_knowledge=True,
    markdown=True,
    show_tool_calls=True
)
electronics_agent.knowledge.load(recreate=False)

electronics_agent.print_response("qual o peso do Eletrodomesticos Pro 300")