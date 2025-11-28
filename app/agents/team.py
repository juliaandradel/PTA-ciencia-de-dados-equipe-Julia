from agno.team import Team

from .agente1 import agente1
from .agente2 import agente2

team = Team(
    name="Example Team",
    mode="route",
    members=[agente1, agente2],
    instructions="This team is designed to handle example tasks.",
    show_members_responses=True
)