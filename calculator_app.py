import streamlit as st
import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y
def percentage(x, y): return (x * y) / 100
def square_root(x): return "Error! Cannot take square root of a negative number." if x < 0 else math.sqrt(x)
def power(x, y): return x ** y

def calculator(operation, num1, num2=None):
    if operation == "Add":
        return add(num1, num2)
    elif operation == "Subtract":
        return subtract(num1, num2)
    elif operation == "Multiply":
        return multiply(num1, num2)
    elif operation == "Divide":
        return divide(num1, num2)
    elif operation == "Percentage":
        return percentage(num1, num2)
    elif operation == "Square Root":
        return square_root(num1)
    elif operation == "Power":
        return power(num1, num2)

# Streamlit UI
st.title("Calculator")

operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide", "Percentage", "Square Root", "Power"])
num1 = st.number_input("Enter first number:", format="%.5f")
if operation != "Square Root":
    num2 = st.number_input("Enter second number:", format="%.5f")
else:
    num2 = None

if st.button("Calculate"):
    result = calculator(operation, num1, num2)
    st.write(f"Result: {result}")
