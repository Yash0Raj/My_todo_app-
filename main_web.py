import streamlit as St
import functions


todos = functions.get_todos()


def add_todo():
    todo_func = St.session_state["new_todo"] + "\n"
    todos.append(todo_func.title())
    functions.write_todos(todos)


St.title("My To-Do App")
St.subheader("Tips for you: ")
St.write("1:- Check a box to remove a To-Do.")
St.write("2:- Add a new To-Do in the box given below.")

for index, todo in enumerate(todos):
    checkbox = St.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del St.session_state[todo]
        St.experimental_rerun()

St.text_input(label=" ", placeholder="Add a new To-Do......",
              on_change=add_todo, key="new_todo")
