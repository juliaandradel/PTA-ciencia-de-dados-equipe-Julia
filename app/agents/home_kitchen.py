from agno.agent import Agent
from agno.models.google import Gemini
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.lancedb import LanceDb
from agno.embedder.google import GeminiEmbedder

# Define onde o conhecimento fica guardado
home_knowledge = PDFKnowledgeBase(
    path="knowledge_base/home_kitchen",
    vector_db=LanceDb(
        table_name="home_kitchen_knowledge",
        uri="tmp/lancedb",
        embedder=GeminiEmbedder(id="models/text-embedding-004"),
    ),
)

# Carrega os PDFs
home_knowledge.load(recreate=False)

home_kitchen_agent = Agent(
    name="Home & Kitchen Specialist",
    role="Especialista em Casa e Cozinha da O-Market",
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="Você ajuda clientes a escolherem os melhores utensílios e decoração.",
    instructions=[
        "Ao responder, PRIMEIRO busque no seu conhecimento (knowledge base).",
        "Foque em materiais, cuidados e dimensões.",
        "Cite a fonte (o nome do arquivo PDF) sempre que possível.",
    ],
    knowledge=home_knowledge,
    search_knowledge=True,
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)