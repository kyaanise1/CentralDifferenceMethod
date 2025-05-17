import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import math
import os
import requests
import base64

st.set_page_config(layout="wide")

img_assets = {
    "title": {
        "url": "https://thumbs.dreamstime.com/b/pink-calculator-illustration-vector-white-background-v-260375892.jpg",
        "path": "images/calculator.jpg"
    },
    "results": {
        "url": "https://cdn-icons-png.flaticon.com/512/17480/17480789.png",
        "path": "images/results.png"
    },
    "plot": {
        "url": "https://images.vexels.com/media/users/3/199956/isolated/preview/c82c099cfab6cb2fd755610dbc6262ca-growing-graph-icon-stroke-pink.png",
        "path": "images/plot.png"
    }
}

os.makedirs("images", exist_ok=True)
for key, val in img_assets.items():
    if not os.path.isfile(val["path"]):
        with open(val["path"], "wb") as f:
            f.write(requests.get(val["url"]).content)

def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.markdown(
    """
    <style>
        body {
            background-color: #FFF3F2;
        }
        .stApp {
            background-color: #FFF3F2;
        }
        .stTextInput input,
        .stNumberInput input,
        .stRadio div[role="radiogroup"] > label {
            background-color: white !important;
        }
        .element-container input {
            background-color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

title_img = get_image_base64(img_assets["title"]["path"])
st.markdown(f"""
<div style="display: flex; align-items: center; gap: 12px;">
    <img src="data:image/jpeg;base64,{title_img}" width="50">
    <h2 style="margin: 0;"><strong>Central Difference Method Calculator</strong></h2>
</div>
""", unsafe_allow_html=True)

st.markdown("Estimate the derivative of a function using the Central Difference Method.")

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# INPUTS with blank defaults
function_str = st.text_input("Enter the function f(x):", value="")
x_unit = st.radio("Select the unit of x:", ["Radians", "Degrees"], horizontal=True)
x_val_str = st.text_input("Enter the point x (e.g., pi/2, 1.57, 180):", value="")
h = st.number_input("Enter the step size h:", value=0.0, format="%.5f")

if function_str.strip() and x_val_str.strip():
    if h == 0.0:
        st.warning("⚠️ Please enter a non-zero step size `h`.")
        st.stop()

    try:
        x_val_input = eval(x_val_str, {"np": np, "math": math, "pi": np.pi})
        x_val = np.radians(x_val_input) if x_unit == "Degrees" else x_val_input
    except:
        st.error("❌ Invalid input for x. Try expressions like `pi`, `3*pi/2`, or `180`.")
        st.stop()

    x_sym = sp.Symbol("x")
    try:
        f_sym = sp.sympify(function_str)
        f_prime_sym = sp.diff(f_sym, x_sym)

        f = sp.lambdify(x_sym, f_sym, modules=["numpy"])
        df_exact = sp.lambdify(x_sym, f_prime_sym, modules=["numpy"])

        derivative = central_difference(f, x_val, h)
        exact = df_exact(x_val)
        error = abs(derivative - exact)

        results_img = get_image_base64(img_assets["results"]["path"])
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 10px; margin-top: 30px;">
            <img src="data:image/png;base64,{results_img}" width="35">
            <h3 style="margin: 0;">Result</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write(f"**Function**: $f(x) = {sp.latex(f_sym)}$")
        st.write(f"**Symbolic derivative**: $f'(x) = {sp.latex(f_prime_sym)}$")
        st.write(f"**Estimated derivative at x = {x_val_input} ({x_unit}) using Central Difference:** `{derivative:.6f}`")
        st.write(f"**Exact derivative at x = {x_val_input} ({x_unit}):** `{exact:.6f}`")
        st.write(f"**Absolute error**: `{error:.6e}`")

        plot_img = get_image_base64(img_assets["plot"]["path"])
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 10px; margin-top: 30px;">
            <img src="data:image/png;base64,{plot_img}" width="35">
            <h3 style="margin: 0;">Function Plot</h3>
        </div>
        """, unsafe_allow_html=True)

        x_vals = np.linspace(x_val - 1.5, x_val + 1.5, 300)
        y_vals = f(x_vals)

        y0 = f(x_val)
        tangent_line = derivative * (x_vals - x_val) + y0

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x_vals, y_vals, label="f(x)", linewidth=2)
        ax.plot(x_vals, tangent_line, 'r--', label="Central Diff Tangent", linewidth=1.8)
        ax.plot(x_val, y0, 'ro', label=f"x = {x_val_input}")
        # Removed vertical line at x = 0

        ax.set_title("Function and Tangent Line at x")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        st.pyplot(fig)

        # ✅ Summary table at the bottom
        st.markdown("### 🖋️ Summary")
        st.markdown(f"""
        | Quantity                      | Value |
        |------------------------------|-------|
        | Function                     | $f(x) = {sp.latex(f_sym)}$ |
        | Symbolic Derivative          | $f'(x) = {sp.latex(f_prime_sym)}$ |
        | Central Difference Estimate  | `{derivative:.6f}` |
        | Exact Derivative             | `{exact:.6f}` |
        | Absolute Error               | `{error:.6e}` |
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
else:
    st.info("Please enter the function, point x, and non-zero step size h to see results.")
