from dotenv import load_dotenv
load_dotenv()

from app.knowledge import electronics_knowledge, home_knowledge

def run_ingestion():
    print("--- INICIANDO INGESTÃO DE CONHECIMENTO ---")
    
    print("1. Processando Eletrônicos...")
    try:
        electronics_knowledge.load(recreate=True) # recreate=True força a limpeza e leitura nova
        print("✅ Eletrônicos indexados com sucesso!")
    except Exception as e:
        print(f"❌ Erro em Eletrônicos: {e}")

    print("\n2. Processando Casa e Cozinha...")
    try:
        home_knowledge.load(recreate=True)
        print("✅ Casa e Cozinha indexados com sucesso!")
    except Exception as e:
        print(f"❌ Erro em Casa e Cozinha: {e}")

if __name__ == "__main__":
    run_ingestion()