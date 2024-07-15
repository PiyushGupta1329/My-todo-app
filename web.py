import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    # session state is a dictionary type
    # put key value here

#import functions helps us to get todo list as functions works as backend and provide us data

#this is use dto make a webaapp interface for user
# we cannot directly run this file to run this we had to go on terminal and type

#stremlit run filename.py this will gave url and open our web app

st.title("My To-Do App")

# st.subheader("this os my todo app")
# st.write("this is my first app")

for todo in todos:
    checkbox=st.checkbox(todo, key=todo)# give checkboxes
    if checkbox:
        todos.pop()
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

#st.text_input(label="Enter a Todo: ")
st.text_input(label="enter",placeholder="Enter Your To-Do...",
              on_change=add_todo,key='new_todo')

# we create pip freeze > requirements.txt file as we had tos how our project publicly so w use that method

