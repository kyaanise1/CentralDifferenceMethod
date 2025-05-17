# Central Difference Method Calculator

**Central Difference Method**, a finite difference technique commonly used in numerical differentiation.

## 📌 Method Explanation

The **Central Difference Method** is a second-order accurate formula used to approximate the derivative of a function:

\[
f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}
\]

Where:
- \( f(x) \) is the function
- \( x \) is the point at which the derivative is estimated
- \( h \) is a small step size

This method is preferred over forward or backward differences due to its improved accuracy and symmetry around the point \( x \).

---

## 🚀 How to Run the App

### Prerequisites:
Ensure the following Python libraries are installed:

```bash
pip install streamlit numpy matplotlib sympy requests
```

### Run the Application:

```bash
streamlit run app.py
```

This will open the app in your default web browser.

---

## 🛠 Features

- Input any valid mathematical function \( f(x) \)
- Choose between radians or degrees for the input point
- View both estimated and exact symbolic derivatives
- Visualize the function with a tangent line from the central difference estimation
- Get error analysis (absolute error)

---

## ✅ Sample Inputs & Outputs

### Example 1:
- **Function**: `sin(x)`
- **Unit**: Radians
- **x**: `pi/4`
- **h**: `0.01`

**Expected Output**:
- Estimated Derivative: ~0.7071
- Exact Derivative: ~0.7071
- Absolute Error: Very small (~1e-7)

### Example 2:
- **Function**: `x**2 + 3*x + 2`
- **Unit**: Degrees
- **x**: `45`
- **h**: `0.01`

**Expected Output**:
- Estimated Derivative: ~4.3702
- Exact Derivative: ~4.3702
- Absolute Error: Near 0

---

## 📁 Submission Contents

- `app.py`: Streamlit application
- `images/`: Folder containing required image assets (downloaded at runtime)
- `README.md`: This file
