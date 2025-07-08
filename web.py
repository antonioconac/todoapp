import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    do = st.session_state["new_todo"] + "\n"
    todos.append(do)
    functions.write_todos(todos + "\n")


st.title("My todo app")
st.subheader("This is my todo app: ")
st.write("This app is to increase productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="asd", placeholder="Add new todo:...",
              on_change=add_todo, key="new_todo")

st.session_state