import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING_V2"]= "true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

## prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "you are an helpful assistant. please respond to the questions asked by the user."),
        ("user", "Question: {question}"),
    ]
)

## Streamlit framwork:
st.title("Gemma model Chatbot with Langchain")
input_text=st.text_input("Enter your question:")

## call the ollam model:
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))



