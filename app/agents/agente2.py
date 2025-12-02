from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools
from agno.agent import  Agent
from dotenv import load_dotenv

load_dotenv()
agent = Agent(
    model = Gemini(id = "models/gemini-2.5-flash"),
    tools = [TavilyTools()],
)

agent.print_response("Qual a data de nascimento do cantor Roberto Carlos")