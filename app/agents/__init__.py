from agno.agent import Agent
from agno.models.google import Gemini
from agno.playground import Playground, serve_playground_app
from .electronics import electronics_agent
from .home_kitchen import home_kitchen_agent

# Agente Genérico
general_agent = Agent(
    name="Agent_Geral",
    role="Atendente Geral",
    model=Gemini(id="models/gemini-1.5-flash"), # <--- AQUI
    instructions="Responda cordialmente a saudações e dúvidas que não sejam sobre produtos específicos."
)

# O TIME (Roteador)
team = Agent(
    name="O-Market Team",
    model=Gemini(id="models/gemini-1.5-flash"), # <--- E AQUI
    team=[electronics_agent, home_kitchen_agent, general_agent],
    instructions=[
        "Você é o Gerente de Inteligência da O-Market.",
        "Sua missão é receber a pergunta e delegar para o agente correto:",
        "1. Dúvidas técnicas/eletrônicos -> chame o 'Agent_Tecnologia'.",
        "2. Dúvidas de casa/móveis -> chame o 'Agent_Casa_Conforto'.",
        "3. Oi/Saudações/Outros -> chame o 'Agent_Geral'.",
        "Não responda perguntas de produtos você mesmo, SEMPRE delegue."
    ],
    markdown=True,
    show_tool_calls=True
)