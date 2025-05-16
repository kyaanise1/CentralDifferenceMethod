import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Central Difference Method Function
def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Streamlit App
st.title("Central Difference Method Calculator")

st.write("This app estimates the derivative of a function using the Central Difference Method.")

# User Inputs
function_str = st.text_input("Enter the function f(x):", "np.sin(x)")
x_val = st.number_input("Enter the point x at which to differentiate:", value=1.0)
h = st.number_input("Enter the step size h:", value=0.01)
exact_derivative_str = st.text_input("(Optional) Enter the exact derivative f'(x):", "np.cos(x)")

# Evaluate function
try:
    f = lambda x: eval(function_str)
    df_exact = lambda x: eval(exact_derivative_str) if exact_derivative_str else None

    derivative = central_difference(f, x_val, h)

    st.subheader("Result")
    st.write(f"Estimated derivative at x = {x_val} is: **{derivative:.6f}**")

    if exact_derivative_str:
        exact = df_exact(x_val)
        error = abs(derivative - exact)
        st.write(f"Exact derivative: **{exact:.6f}**")
        st.write(f"Absolute Error: **{error:.6e}**")

    # Visualization
    st.subheader("Visualization")
    x_vals = np.linspace(x_val - 5*h, x_val + 5*h, 100)
    y_vals = f(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='f(x)')
    ax.plot(x_val, f(x_val), 'ro', label='x')
    ax.set_title("Function Plot")
    ax.legend()
    st.pyplot(fig)

except Exception as e:
    st.error(f"Error evaluating function: {e}")
