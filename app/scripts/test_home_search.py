# app/scripts/test_home_search.py

from app.knowledge import home_knowledge

def main():
    query = "SKU Alimentos Plus 100"

    # sua versão não aceita limit=...
    docs = home_knowledge.search(query)

    print(f"Total de documentos encontrados: {len(docs)}")
    # limita “na mão” aos 5 primeiros
    for i, d in enumerate(docs[:5]):
        source = d.metadata.get("source") if d.metadata else None
        preview = (d.text or "").replace("\n", " ")[:200]
        print(f"\n=== DOC {i} ===")
        print("Fonte:", source)
        print("Trecho:", preview)

if __name__ == "__main__":
    main()
