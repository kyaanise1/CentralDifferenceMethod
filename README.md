# Central Difference Method Calculator

This Streamlit app estimates the derivative of a function at a given point using the **Central Difference Method**, a widely used finite difference approach in numerical calculus.

---

## 📌 Method Explanation

The **Central Difference Method** is a second-order numerical technique for estimating the first derivative of a function:

\[
f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}
\]

Where:
- \( f(x) \): the input function
- \( x \): the evaluation point
- \( h \): a small positive step size

This method is more accurate than forward or backward difference methods because it averages the slope from both directions, minimizing error.

---

## 🚀 How to Run the App

### 1. Prerequisites

Install the required Python packages:

```bash
pip install streamlit numpy matplotlib sympy requests
```

### 2. Run the App

Use the following command:

```bash
streamlit run app.py
```

This will open the application in your browser.

---

## 🛠 Features

- User input for:
  - Function \( f(x) \)
  - Evaluation point \( x \) (in radians or degrees)
  - Step size \( h \)
- Visual output of:
  - Original function
  - Central difference tangent line
- Displays:
  - Symbolic derivative (via SymPy)
  - Central difference approximation
  - Exact derivative
  - Absolute error
  - Summary table of all results
- Custom styled interface with relevant icons and illustrations

---

## ✅ Sample Inputs & Expected Outputs

### Example 1:
- **Function**: `cos(4*x)`
- **Unit**: Radians
- **x**: `pi/6`
- **h**: `0.01`

**Expected Output**:
- Central Difference Estimate: ~-3.46318  
- Exact Derivative: ~-3.46410  
- Absolute Error: ~9.236865e-04 or 0.00092

---

### Example 2:
- **Function**: `2*x**3 + x**2 - 4`
- **x**: `2.5`
- **h**: `0.5`

**Expected Output**:
- Central Difference Estimate: ~43.000000  
- Exact Derivative: ~42.500  
- Absolute Error: ~5.000000e-01 or 0.500000

---

## 📁 Submission Contents

- `app.py` — Main Streamlit application
- `README.md` — This file

---

## 🧠 Notes

- Step size `h` **must be non-zero**, or the app will not run the calculation.
- Mathematical expressions for \( x \) like `pi`, `pi/2`, `3*pi/4`, or `180` are supported.
- All functions must be valid Python expressions parseable by `sympy.sympify()`.

---

Feel free to customize this app further with more numerical methods or error analysis!
