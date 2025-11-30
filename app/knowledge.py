from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.lancedb import LanceDb
from agno.knowledge.embedder.google import GeminiEmbedder

# Definição do Conhecimento de Eletrônicos
electronics_knowledge = PDFKnowledgeBase(
    path="knowledge_base/electronics",
    vector_db=LanceDb(
        table_name="electronics_knowledge",
        uri="tmp/lancedb",
        embedder=GeminiEmbedder(id="models/text-embedding-004"),
    ),
)

# Definição do Conhecimento de Casa e Cozinha
home_knowledge = PDFKnowledgeBase(
    path="knowledge_base/home_kitchen",
    vector_db=LanceDb(
        table_name="home_kitchen_knowledge",
        uri="tmp/lancedb",
        embedder=GeminiEmbedder(id="models/text-embedding-004"),
    ),
)