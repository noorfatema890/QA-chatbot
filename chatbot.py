import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(), override=True)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's questions."),
    ("user", "Question: {question}")
])

# Generate Response Function
def generate_response(question, api_key, engine, temperature, max_token):
    llm = ChatGroq(
    model=engine,
    groq_api_key=api_key,
    temperature=temperature,
    max_tokens=max_token
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# ----------- Streamlit UI -----------

st.title("Enhanced Q&A Chatbot With Gemini")
st.write("Go ahead and ask any question")

# Sidebar Settings
st.sidebar.title("Settings")

api_key = st.sidebar.text_input(
    "Enter your Gemini API Key:",
    type="password"
)

engine = st.sidebar.selectbox(
    "Select Model",
    ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "gemma2-9b-it"]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7
)

max_token = st.sidebar.slider(
    "Max Tokens",
    min_value=50,
    max_value=300,
    value=150
)

# Main Input
user_input = st.text_input("You:")

if user_input:
    if not api_key:
        st.warning("Please enter your Gemini API Key in the sidebar.")
    else:
        response = generate_response(user_input, api_key, engine, temperature, max_token)
        st.write(response)
else:
    st.write("Please provide the user input")