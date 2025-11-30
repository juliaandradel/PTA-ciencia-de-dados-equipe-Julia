from dotenv import load_dotenv
load_dotenv()

from agno.playground import Playground
from app.agents import team
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# 1. Cria o Playground
playground = Playground(agents=[team])

# 2. Transforma em App
app = playground.get_app()

# 3. O PULO DO GATO: Forçar liberação total de segurança (CORS)
# Isso permite que o site https://app.agno.com converse com seu PC
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Aceita conexões de qualquer lugar
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    print("--- SERVIDOR INICIADO ---")
    print("Link para o Playground: https://app.agno.com/playground?endpoint=http://127.0.0.1:7777/v1")
    
    # Rodamos o servidor manualmente
    uvicorn.run(app, host="127.0.0.1", port=7777)