import streamlit as st

# --- App Title ---
st.title("Welcome to My Python App")

st.markdown(
    """
    This app runs a simple Python function and shows the code used — but you can't edit it.
    """
)

# --- Your Python Code / Logic ---
def greet(name):
    return f"Hello, {name}!"

# --- User Input ---
name = st.text_input("Enter your name:")

# --- Output ---
if name:
    st.success(greet(name))

# --- Show the code (read-only) ---
with st.expander("📄 See the code used"):
    st.code(
        '''
def greet(name):
    return f"Hello, {name}!"

name = input("Enter your name: ")
if name:
    print(greet(name))
        ''',
        language="python"
    )
