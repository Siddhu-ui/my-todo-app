import streamlit as st
import functions
#from webapp import checkbox, index


#from webapp import add_todo

def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    if todo_local not in todos:
        todos.append(todo_local)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my Todo App.")
st.write("This app is to increase your productivity")

for index,todo in enumerate(todos):

    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_user

st.text_input(label="",placeholder = "Add new todo...",
              on_change=add_todo, key='new_todo')
