import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    do = st.session_state["new_todo"] + "\n"
    todos.append(do)
    functions.write_todos(todos)


st.title("My todo app")
st.subheader("This is my todo app: ")
st.write("This app is to increase productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add new to-do", placeholder="Add new todo:...",
              on_change=add_todo, key="new_todo")
