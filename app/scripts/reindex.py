from pathlib import Path
from app.knowledge import (
    electronics_knowledge,
    home_knowledge,
    electronics_vector_db,
    home_vector_db,
    pdf_reader,
)

# raiz do projeto (onde estão app/ e knowledge_base/)
BASE_DIR = Path(__file__).resolve().parents[2]

electronics_path = BASE_DIR / "knowledge_base" / "electronics"
home_path = BASE_DIR / "knowledge_base" / "home_kitchen"

def main():
    print("\nRecriando RAG estático (electronics + home_kitchen)...")

    electronics_vector_db.drop()
    home_vector_db.drop()

    electronics_vector_db.create()
    home_vector_db.create()

    electronics_knowledge.add_content(
        path=str(electronics_path),
        reader=pdf_reader,
    )

    home_knowledge.add_content(
        path=str(home_path),
        reader=pdf_reader,
    )

    print("\nO RAGA foi atualizado!!!\n")

if __name__ == "__main__":
    main()
