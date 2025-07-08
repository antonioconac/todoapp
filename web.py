import streamlit as st
from modules import functions

todos = functions.get_todos()

st.title("My todo app")
st.subheader("This is my todo app: ")
st.write("This app is to increase productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo:...")