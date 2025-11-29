from agno.agent import Agent
from agno.models.google import Gemini
from .electronics import electronics_agent
from .home_kitchen import home_kitchen_agent

# Criamos um Agente Líder que tem acesso aos especialistas
team = Agent(
    name="O-Market Team",
    model=Gemini(id="gemini-2.0-flash-exp"),
    instructions=[
        "Você é o gerente de produtos da O-Market.",
        "Se a pergunta for sobre eletrônicos, celulares ou computadores, delegue para o 'Electronics Specialist'.",
        "Se a pergunta for sobre utensílios, móveis ou decoração, delegue para o 'Home & Kitchen Specialist'.",
        "Se for um 'oi' ou pergunta geral, responda você mesmo de forma cordial."
    ],
    # Aqui é onde a mágica acontece: passamos os agentes que criamos como um time
    team=[electronics_agent, home_kitchen_agent],
    markdown=True,
    show_tool_calls=True
)