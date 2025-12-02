from agno.agent import Agent
from agno.models.google import Gemini


# Importa os agentes que criamos
from .electronics import electronics_agent
from .home_kitchen import home_kitchen_agent

# Agente Genérico (Davi) para coisas que não se encaixam
general_agent = Agent(
    name="Agent_Geral",
    role="Atendente Geral",
    model=Gemini(id="gemini-1.5-flash-002"),
    instructions="Responda cordialmente a saudações e dúvidas que não sejam sobre produtos específicos."
)

"""
# O TIME (Roteador)
team = Agent(
    name="O-Market Team",
    model=Gemini(id="gemini-1.5-flash-002"),
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
"""