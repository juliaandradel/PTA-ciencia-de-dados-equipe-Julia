from pathlib import Path
from agno.knowledge.reader.pdf_reader import PDFReader

BASE_DIR = Path(__file__).resolve().parent
ELECTRONICS_DIR = BASE_DIR / "knowledge_base" / "electronics"

reader = PDFReader()
first_pdf = next(ELECTRONICS_DIR.glob("*.pdf"))

docs = reader.read(pdf=str(first_pdf))

print("Total de chunks (Document) lidos:", len(docs))
for i, doc in enumerate(docs):
    print(f"\n=== CHUNK {i} ===")
    # se for objeto Document, acessa .content
    try:
        text = doc.content
    except AttributeError:
        text = doc
    print(str(text)[:500])  # só os primeiros 500 caracteres
