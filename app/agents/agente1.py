from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools
from agno.agent import  Agent
from dotenv import load_dotenv
from app.tools.ferramenta1 import formatar_data

load_dotenv()
agente1 = Agent(
    model = Gemini(id = "models/gemini-2.5-flash"),
    tools = [TavilyTools(),formatar_data],
)

agente1.print_response("Qual a data de nascimento do cantor Roberto Carlos")