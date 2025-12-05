# app/knowledge.py
from pathlib import Path
import os
from dotenv import load_dotenv

from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.vectordb.chroma import ChromaDb

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

gemini_embedder = GeminiEmbedder(
    id="models/text-embedding-004",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

CHROMA_PATH = str(BASE_DIR / "tmp" / "chromadb")

electronics_vector_db = ChromaDb(
    collection="electronics_knowledge",
    path=CHROMA_PATH,
    persistent_client=True,
    embedder=gemini_embedder,
)

home_vector_db = ChromaDb(
    collection="home_kitchen_knowledge",
    path=CHROMA_PATH,
    persistent_client=True,
    embedder=gemini_embedder,
)

electronics_knowledge = Knowledge(
    name="electronics_knowledge",
    vector_db=electronics_vector_db,
)

home_knowledge = Knowledge(
    name="home_kitchen_knowledge",
    vector_db=home_vector_db,
)

pdf_reader = PDFReader()

def init_knowledge(load_electronics=True, load_home=True):
    if load_electronics:
        electronics_knowledge.add_content(
            path=str(BASE_DIR / "knowledge_base" / "electronics"),
            reader=pdf_reader,
        )

    if load_home:
        home_knowledge.add_content(
            path=str(BASE_DIR / "knowledge_base" / "home_kitchen"),
            reader=pdf_reader,
        )