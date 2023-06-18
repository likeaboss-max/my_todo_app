import streamlit as st
import functions

todos = functions.get_todos()

st.subheader("This is my todo app.")
st.write("Increase your productivity")
st.title("My Todo App")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add a new todo....")
print("Hello")