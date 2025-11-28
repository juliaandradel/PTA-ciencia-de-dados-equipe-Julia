from agno.models.google import Gemini
from agno.tools.tavily import TavilyTools
from agno.agent import  Agent
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
import re

load_dotenv()

db = SqliteDb(db_file="tmp/data.db")

def formatar_data(texto: str) -> str:
    """
    Extrai uma data escrita em formato textual de uma resposta em português
    (por exemplo: 'A data de nascimento do cantor Roberto Carlos é 19 de abril de 1941.')
    e devolve a mesma data formatada no padrão dd/mm/aaaa (por exemplo: '19/04/1941').
    Use esta ferramenta sempre que precisar padronizar datas extraídas de texto livre.
    """
    meses = {
        "janeiro": "01",
        "fevereiro": "02",
        "marco": "03",
        "março": "03",
        "abril": "04",
        "maio": "05",
        "junho": "06",
        "julho": "07",
        "agosto": "08",
        "setembro": "09",
        "outubro": "10",
        "novembro": "11",
        "dezembro": "12",
    }

    m = re.search(r"(\d{1,2}) de ([a-zç]+) de (\d{4})", texto.lower())
    if not m:
        return texto  # se não achar padrão, devolve o texto original

    dia_str, mes_nome, ano_str = m.groups()
    dia = dia_str.zfill(2)
    mes = meses.get(mes_nome, "01")

    return f"{dia}/{mes}/{ano_str}"


agent = Agent(
    model = Gemini(id = "models/gemini-2.5-flash"),
    tools = [TavilyTools(),
             formatar_data],
    db=db,
    add_history_to_context=True,
    num_history_runs=4
)

agent.print_response("Qual a data de nascimento do cantor Manoel Gomes")
agent.print_response("Qual a data de nascimento do jogador de futebol Neymar")
agent.print_response("Quais foram as pessoas que eu perguntei a data de nascimento")