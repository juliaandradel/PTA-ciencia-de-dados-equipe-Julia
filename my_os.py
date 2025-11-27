from agno.agent import Agent
from agno.models.google import Gemini
from agno.db.sqlite import AsyncSqliteDb
from agno.os import AgentOS
from dotenv import load_dotenv

load_dotenv()

assistant = Agent(
    name="Assistant",
    model=Gemini(id="models/gemini-2.5-flash"),
    db=AsyncSqliteDb(db_file="my_os.db"),
    instructions=["You are a helpful AI assistant."],
    markdown=True,
)

agent_os = AgentOS(
    id="my-first-os",
    description="My first AgentOS",
    agents=[assistant],
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="my_os:app", reload=True)
