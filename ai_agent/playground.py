from agno.agent import Agent
from agno.playground import Playground, serve_playground_app
from agno.models.groq import Groq
from agno.vectordb.lancedb import LanceDb
from agno.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.knowledge import AgentKnowledge
from dotenv import load_dotenv
import os

load_dotenv()

# --- CONFIGURAÇÃO IGUAL AO KNOWLEDGE.PY ---
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "tmp", "lancedb")

embedder = SentenceTransformerEmbedder(model="all-MiniLM-L6-v2")

vector_db = LanceDb(
    table_name="produtos_knowledge",
    uri=db_path,
    embedder=embedder
)

# Conecta o banco ao agente
knowledge_base = AgentKnowledge(vector_db=vector_db)

# --- AGENTE ---
agent = Agent(
    name="Especialista O-Market",
    role="Responder perguntas técnicas sobre produtos baseado nos manuais PDF.",
    model=Groq(id="llama3-8b-8192"),
    knowledge=knowledge_base,
    search_knowledge=True,
    markdown=True
)

app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)