from dotenv import load_dotenv
load_dotenv()

from app.agents import team

print("--- INICIANDO TESTE DOS AGENTES ---")
print("Perguntando sobre o PDF de Artes...")

# Aqui ele vai simular o chat direto no terminal
team.print_response(
    "Resuma o que o documento fala sobre a Arte Rupestre (ou qualquer tema do seu PDF de artes)", 
    stream=True, 
    show_full_messages=True
)