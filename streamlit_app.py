import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

st.set_page_config(page_title="Central Difference Method Calculator", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #FFF3F2;
        padding: 2rem 4rem 4rem 4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧮 Central Difference Method Calculator")
st.write("Estimate the derivative of a function using the Central Difference Method.")

# Function input
func_str = st.text_input("Enter the function f(x):", "sin(x)")

# Unit selection
unit = st.radio("Select the unit of x:", ("Radians", "Degrees"))

# Point input
x_val_input = st.text_input("Enter the point x (e.g., pi/2, 1.57, 180):", "pi/2")

# Step size input
h = st.number_input("Enter the step size h:", min_value=1e-6, max_value=1.0, value=0.01, format="%.5f")

# Parse and prepare function safely
def parse_function(func_str):
    # Allowed names for eval
    allowed_names = {
        k: v for k, v in math.__dict__.items() if not k.startswith("__")
    }
    allowed_names['x'] = 0  # placeholder

    def f(x):
        allowed_names['x'] = x
        try:
            return eval(func_str, {"__builtins__": {}}, allowed_names)
        except Exception as e:
            st.error(f"Error evaluating function: {e}")
            return None
    return f

f = parse_function(func_str)

# Parse x input (allow pi, fractions like pi/2)
def parse_x(x_str):
    try:
        # Replace pi with math.pi, handle fractions
        x_str = x_str.replace("pi", f"{math.pi}")
        return float(eval(x_str, {"__builtins__": {}}, {}))
    except Exception as e:
        st.error(f"Error parsing x input: {e}")
        return None

x_val = parse_x(x_val_input)

if x_val is not None and f(x_val) is not None:
    # Convert degrees to radians if needed
    if unit == "Degrees":
        x_val = math.radians(x_val)

    # Central difference method for derivative
    derivative = (f(x_val + h) - f(x_val - h)) / (2 * h)

    st.subheader("📊 Result")
    st.write(f"Estimated derivative at x = {x_val_input} ({unit}):")
    st.write(f"f'(x) ≈ {derivative:.6f}")

    # Plot function around x=0, range -2 to 2
    x_vals = np.linspace(-2, 2, 400)
    y_vals = np.array([f(x) for x in x_vals])

    fig, ax = plt.subplots(figsize=(6, 4))  # smaller figure size

    ax.plot(x_vals, y_vals, label="f(x)")
    # Highlight the input point, converting back to original units for label
    if unit == "Degrees":
        x_val_plot = x_val  # plotted in radians, no conversion
    else:
        x_val_plot = x_val
    ax.plot(x_val_plot, f(x_val_plot), 'ro', label=f"x = {x_val_input}")

    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)

    ax.set_title("Function Around x = 0")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    st.pyplot(fig)
else:
    st.info("Please enter a valid function and point x to see the derivative and plot.")
