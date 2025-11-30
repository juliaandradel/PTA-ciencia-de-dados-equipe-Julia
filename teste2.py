from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools
from agno.agent import Agent
from dotenv import load_dotenv
import os

load_dotenv()

# Verifica se tem chave do Tavily (o código do seu amigo usa)
api_key = os.getenv("TAVILY_API_KEY")
tools_list = []
if api_key:
    tools_list = [TavilyTools()]
else:
    print("AVISO: Chave TAVILY_API_KEY não encontrada no .env. Rodando sem Tavily.")

try:
    # TENTATIVA 1: O Modelo (2.5)
    print("Tentando rodar com models/gemini-2.5-flash...")
    agent = Agent(
        model = Gemini(id = "models/gemini-2.5-flash"),
        tools = tools_list,
        markdown=True
    )
    agent.print_response("Qual a data de nascimento do cantor Roberto Carlos")

except Exception as e:
    print(f"\n❌ Ocorreu um erro com o 2.5: {e}")
    print("\nTentando com o 1.5 (o padrão)...")
    
    # TENTATIVA 2: O Padrão (1.5) com o prefixo models/
    try:
        agent = Agent(
            model = Gemini(id = "models/gemini-1.5-flash"),
            tools = tools_list,
            markdown=True
        )
        agent.print_response("Qual a data de nascimento do cantor Roberto Carlos")
    except Exception as e2:
         print(f"\n❌ Erro total: {e2}")