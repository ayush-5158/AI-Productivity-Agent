#---------------- This is for terminal CLI version----------------



from dotenv import load_dotenv
load_dotenv()
from rich import print
from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from tools.calculator import calculator
from tools.date_and_time import get_date
from tools.dice_and_coin import dice,coin
from tools.middle import middle
from tools.password_generator import password_generator
from tools.UUID_generator import uuid_generator

model = ChatMistralAI(model='mistral-small-2506')
tools =[calculator,get_date,dice,coin,password_generator,uuid_generator]
agent = create_agent(model=model,tools=tools,system_prompt="""You are a productivity assistant.

You have access to tools.

Whenever a user's request can be solved using a tool, you MUST use the appropriate tool.

Never perform calculations yourself.

Always use the calculator tool for arithmetic.""",middleware=middle)


while True:
    query = input("You : ").strip()
    if query == 'exit':
        break
    if not query:
        continue
    result = agent.invoke(

        {"messages":[{"role":"user","content": query}]}
    )

    print(f"Bot : {result['messages'][-1].content}")