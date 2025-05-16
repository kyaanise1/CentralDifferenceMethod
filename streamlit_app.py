import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math

# Set the layout to wide to expand the app horizontally
st.set_page_config(layout="wide")

# Inject custom CSS for background color
st.markdown(
    """
    <style>
        body {
            background-color: #FFF3F2;
        }
        .stApp {
            background-color: #FFF3F2;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Central Difference Method
def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Streamlit App Title
st.title("🧮 Central Difference Method Calculator")
st.markdown("Estimate the derivative of a function using the Central Difference Method.")

# Function input
function_str = st.text_input("Enter the function f(x):", value="sin(x)")

# Unit selection for x
x_unit = st.radio("Select the unit of x:", ["Radians", "Degrees"], horizontal=True)

# x input as text for expressions like pi/2, np.pi
x_val_str = st.text_input("Enter the point x (e.g., pi/2, 1.57, 180):", value="pi/2")

# Step size
h = st.number_input("Enter the step size h:", value=0.01, format="%.5f")

try:
    # Parse x input
    x_val_input = eval(x_val_str, {"np": np, "math": math, "pi": np.pi})
    x_val = np.radians(x_val_input) if x_unit == "Degrees" else x_val_input
except:
    st.error("❌ Invalid input for x. Try using expressions like `pi`, `3*pi/2`, or `180`.")
    st.stop()

# Symbolic computation with sympy
x_sym = sp.Symbol("x")
try:
    f_sym = sp.sympify(function_str)
    f_prime_sym = sp.diff(f_sym, x_sym)

    # Lambdify for numerical use
    f = sp.lambdify(x_sym, f_sym, modules=["numpy"])
    df_exact = sp.lambdify(x_sym, f_prime_sym, modules=["numpy"])

    # Numerical estimation
    derivative = central_difference(f, x_val, h)
    exact = df_exact(x_val)
    error = abs(derivative - exact)

    # Display results
    st.subheader("📊 Result")
    st.write(f"**Function**: $f(x) = {sp.latex(f_sym)}$")
    st.write(f"**Symbolic derivative**: $f'(x) = {sp.latex(f_prime_sym)}$")
    st.write(f"**Estimated derivative at x = {x_val_input} ({x_unit})**: `{derivative:.6f}`")
    st.write(f"**Exact derivative**: `{exact:.6f}`")
    st.write(f"**Absolute error**: `{error:.6e}`")

    # Visualization
    st.subheader("📈 Function Plot")

    # Plot range fixed from -3 to 3, centered at 0
    x_vals = np.linspace(-3, 3, 300)
    y_vals = f(x_vals)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x_vals, y_vals, label="f(x)")

    # Highlight the input x point
    ax.plot(x_val, f(x_val), 'ro', label=f"x = {x_val_input}")

    # Vertical line at 0
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)

    ax.set_title("Function Around x = 0")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    st.pyplot(fig)

except Exception as e:
    st.error(f"⚠️ Error: {e}")
