import os
import glob
# Mudança aqui: de 'agno' para 'phi'
from phi.document.reader.pdf import PDFReader
from phi.vectordb.lancedb import LanceDb
from phi.embedder.sentence_transformer import SentenceTransformerEmbedder

# --- CAMINHOS ---
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
pdf_path = os.path.join(project_root, "knowledge_base")
db_path = os.path.join(current_dir, "tmp", "lancedb")

print(f"📂 Lendo de: {pdf_path}")

# --- CÉREBRO ---
embedder = SentenceTransformerEmbedder(model="all-MiniLM-L6-v2")

vector_db = LanceDb(
    table_name="produtos_knowledge",
    uri=db_path,
    embedder=embedder,
)

def carregar():
    # Verifica se a pasta existe
    if not os.path.exists(pdf_path):
        print(f"❌ A pasta '{pdf_path}' não existe!")
        return

    # Procura PDFs
    arquivos = glob.glob(os.path.join(pdf_path, "**/*.pdf"), recursive=True)
    if not arquivos:
        print("❌ Nenhum PDF encontrado.")
        return
    
    print(f"📚 Encontrados {len(arquivos)} manuais.")

    # Lê e processa
    reader = PDFReader()
    docs = []
    for arq in arquivos:
        try:
            # O método read() do PDFReader retorna uma lista de documentos
            lidos = reader.read(arq)
            for d in lidos:
                d.metadata = {"source": os.path.basename(arq)}
            docs.extend(lidos)
            print(f"   ✅ Lido: {os.path.basename(arq)}")
        except Exception as e:
            print(f"   ⚠️ Erro em {os.path.basename(arq)}: {e}")

    # Salva
    if docs:
        vector_db.create(documents=docs, on_exist="overwrite")
        print("✅ SUCESSO! Base criada.")
    else:
        print("⚠️ Nenhum conteúdo válido extraído.")

if __name__ == "__main__":
    carregar()