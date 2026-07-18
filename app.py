#-----------This is a streamlit version of my agent (Code for UI is written by AI)------


from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI

from tools.calculator import calculator
from tools.date_and_time import get_date
from tools.dice_and_coin import dice, coin
from tools.middle import middleman
from tools.password_generator import password_generator
from tools.UUID_generator import uuid_generator


# ---------------------- Page Config ---------------------- #

st.set_page_config(
    page_title="AI Productivity Agent",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 AI Productivity Agent")
st.caption("Powered by LangChain + Mistral")


# ---------------------- Create Agent ---------------------- #

model = ChatMistralAI(model="mistral-small-2506")

tools = [
    calculator,
    get_date,
    dice,
    coin,
    password_generator,
    uuid_generator,
]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
You are a productivity assistant.

You have access to tools.

Whenever a user's request can be solved using a tool, you MUST use the appropriate tool.

Never perform calculations yourself even you know, only use the tools provided to you for what user is asking

Always use the calculator tool for arithmetic.
""",
)


# ---------------------- Chat History ---------------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------------- User Input ---------------------- #

prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ]
                }
            )

            response = result["messages"][-1].content

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )