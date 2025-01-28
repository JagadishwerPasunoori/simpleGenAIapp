import os
from dotenv import load_dotenv
load_dotenv()


import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING_V2"]= "True"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

## prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "you are an helpful assistant. please respond to the questions asked by the user."),
        ("user", "Question: {question}"),
    ]
)

## Streamlit framwork:
st.title("openai model Chatbot with Langchain")
input_text=st.text_input("Enter your question:")

## call the ollam model:
from langchain_openai import ChatOpenAI
llm=ChatOpenAI(model='gpt-4o')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
