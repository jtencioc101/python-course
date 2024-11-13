import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout='wide')

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""
    
    
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This is not meant for prod")

st.text_input(label="Type here:", placeholder=("Add a todo ..."),
             on_change=add_todo, key="new_todo")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()