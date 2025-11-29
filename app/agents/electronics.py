from agno.agent import Agent
from agno.models.google import Gemini
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.lancedb import LanceDb
from agno.embedder.google import GeminiEmbedder

# Define onde o conhecimento fica guardado
electronics_knowledge = PDFKnowledgeBase(
    path="knowledge_base/electronics",  # Pasta dos PDFs
    vector_db=LanceDb(
        table_name="electronics_knowledge",
        uri="tmp/lancedb",  # Pasta temporária onde o banco cria os arquivos
        embedder=GeminiEmbedder(id="models/text-embedding-004"), # Embedder do Google
    ),
)

# Carrega os PDFs na primeira vez que rodar (pode demorar uns segundos na inicialização)
electronics_knowledge.load(recreate=False)

electronics_agent = Agent(
    name="Electronics Specialist",
    role="Especialista técnico em Eletrônicos da O-Market",
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="Você é a autoridade máxima em produtos eletrônicos, computadores e celulares.",
    instructions=[
        "Ao responder, PRIMEIRO busque no seu conhecimento (knowledge base).",
        "Foque em especificações técnicas: processador, memória, voltagem.",
        "Cite a fonte (o nome do arquivo PDF) sempre que possível.",
        "Se não achar no PDF, diga que não consta no manual."
    ],
    knowledge=electronics_knowledge, # <--- Ligamos o conhecimento aqui
    search_knowledge=True,           # <--- Ativamos a busca
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)