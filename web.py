import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo'].strip()
    if not todo:
        return
    todos = functions.get_todos()
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


def complete_todo(idx):
    todos = functions.get_todos()
    if 0 <= idx < len(todos):
        todos.pop(idx)
        functions.write_todos(todos)
        # st.rerun()


st.title("My To-Do App")
st.subheader("This is my to do app.")
st.write("This app is to increase your productivity!")

todos = functions.get_todos()

for index, todo in enumerate(todos):
    st.checkbox(
        todo.strip(),
        key=f"todo_{index}_{hash(todo)}",
        on_change=complete_todo,
        args=(index,)
    )

st.text_input(label="Enter a todo.",
              label_visibility="collapsed",
              placeholder="Enter a todo.",
              on_change=add_todo,
              key="new_todo")

st.write(st.session_state)