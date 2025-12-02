from pathlib import Path

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.vectordb.lancedb import LanceDb

BASE_DIR = Path(__file__).resolve().parent.parent

# Vector DB compartilhado ou separado
electronics_vector_db = LanceDb(
    table_name="electronics_knowledge",
    uri=str(BASE_DIR / "tmp" / "lancedb"),
    embedder=GeminiEmbedder(id="models/text-embedding-004"),
)

home_vector_db = LanceDb(
    table_name="home_kitchen_knowledge",
    uri=str(BASE_DIR / "tmp" / "lancedb"),
    embedder=GeminiEmbedder(id="models/text-embedding-004"),
)

# 1) Cria as knowledge bases (sem documentos ainda)
electronics_knowledge = Knowledge(vector_db=electronics_vector_db)
home_knowledge = Knowledge(vector_db=home_vector_db)

# 2) Adiciona o conteúdo dos PDFs usando PDFReader
electronics_knowledge.add_content(
    path=str(BASE_DIR / "knowledge_base" / "electronics"),
    reader=PDFReader(),
)

home_knowledge.add_content(
    path=str(BASE_DIR / "knowledge_base" / "home_kitchen"),
    reader=PDFReader(),
)

