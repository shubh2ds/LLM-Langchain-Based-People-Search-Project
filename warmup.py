# Using OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Langchain Based People Search')
input_text=st.text_input("Search the topic u want")

## OPENAI LLMS
llm=OpenAI(temperature=0.7)

if input_text:
    st.write(llm(input_text))
