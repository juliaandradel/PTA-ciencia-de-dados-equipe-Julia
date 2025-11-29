from dotenv import load_dotenv
load_dotenv()  # <--- ISSO AQUI LÊ O SEU ARQUIVO .ENV

from agno.playground import Playground, serve_playground_app
from app.agents import team

# Configura o Playground com o nosso time de agentes
playground = Playground(agents=[team])

# Se rodar este arquivo, sobe o servidor
if __name__ == "__main__":
    serve_playground_app("main:playground", reload=True, port=7777)