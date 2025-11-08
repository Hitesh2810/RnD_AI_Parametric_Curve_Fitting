# ================================================
# Assignment: Finding θ, M, X from Parametric Curve
# Author: Hitesh Kumar S
# ================================================

import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Load Data
# -----------------------------
data = pd.read_csv("xy_data.csv")

if 't' in data.columns:
    t_vals = data['t'].values
else:
    n = len(data)
    t_vals = np.linspace(6, 60, n)

x_data = data['x'].values
y_data = data['y'].values

# -----------------------------
# Step 2: Define Parametric Equations
# -----------------------------
def curve(params, t):
    theta, M, X = params
    x = t*np.cos(theta) - np.exp(M*np.abs(t))*np.sin(0.3*t)*np.sin(theta) + X
    y = 42 + t*np.sin(theta) + np.exp(M*np.abs(t))*np.sin(0.3*t)*np.cos(theta)
    return x, y

# -----------------------------
# Step 3: Define L1 Loss Function
# -----------------------------
def loss(params):
    x_pred, y_pred = curve(params, t_vals)
    return np.sum(np.abs(x_pred - x_data) + np.abs(y_pred - y_data))

# -----------------------------
# Step 4: Optimize (Find θ, M, X)
# -----------------------------
bounds = [(0, np.deg2rad(50)), (-0.05, 0.05), (0, 100)]
initial_guess = [np.deg2rad(10), 0.0, 10.0]

result = minimize(loss, initial_guess, bounds=bounds, method='L-BFGS-B')
theta_opt, M_opt, X_opt = result.x

# -----------------------------
# Step 5: Generate Predicted Curve
# -----------------------------
x_pred, y_pred = curve(result.x, t_vals)

# -----------------------------
# Step 6: Save Outputs
# -----------------------------
# 1️⃣ Text Summary
with open("fit_results.txt", "w") as f:
    f.write(f"Best-fit parameters:\n")
    f.write(f"Theta (radians): {theta_opt:.8f}\n")
    f.write(f"Theta (degrees): {np.degrees(theta_opt):.8f}\n")
    f.write(f"M: {M_opt:.8f}\n")
    f.write(f"X: {X_opt:.8f}\n")
    f.write(f"L1 Loss: {result.fun:.8f}\n\n")

    f.write("LaTeX Equation:\n")
    f.write(f"\\left(t\\cos({theta_opt:.8f}) - e^{{{M_opt:.8f}|t|}}"
            f"\\sin(0.3t)\\sin({theta_opt:.8f}) + {X_opt:.8f},"
            f"\\ 42 + t\\sin({theta_opt:.8f}) + e^{{{M_opt:.8f}|t|}}"
            f"\\sin(0.3t)\\cos({theta_opt:.8f})\\right)\n")

# 2️⃣ Plot
plt.figure(figsize=(8,6))
plt.scatter(x_data, y_data, s=10, color='blue', label='Data Points')
plt.plot(x_pred, y_pred, color='red', linewidth=2, label='Fitted Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data vs Fitted Curve')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("data_vs_model.png")
plt.show()

# 3️⃣ Save comparison CSV
pd.DataFrame({
    't': t_vals,
    'x_data': x_data,
    'y_data': y_data,
    'x_pred': x_pred,
    'y_pred': y_pred
}).to_csv("predicted_vs_data.csv", index=False)

# -----------------------------
# Step 7: Print Final Results
# -----------------------------
print("✅ Best-fit Results")
print(f"Theta (radians): {theta_opt:.8f}")
print(f"Theta (degrees): {np.degrees(theta_opt):.8f}")
print(f"M: {M_opt:.8f}")
print(f"X: {X_opt:.8f}")
print(f"L1 Loss: {result.fun:.8f}")
print("\nFiles Generated:")
print(" - fit_results.txt")
print(" - data_vs_model.png")
print(" - predicted_vs_data.csv")
