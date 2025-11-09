# Research and Development / AI – Parameter Estimation Assignment

### Name: Hitesh Kumar S  
### Department: Computer Science and Engineering  
### Register Number: BL.EN.U4CSE20058

---

## 🧾 Abstract

This project focuses on estimating the unknown parameters **θ**, **M**, and **X** in a given parametric curve equation. Using optimization techniques and numerical fitting, the parameters were determined such that the model closely matches provided dataset points. The process includes data analysis, loss minimization using SciPy, and result visualization through Matplotlib. The final model shows a strong correlation between predicted and given data.

---

## 📘 Basic Assignment Rules

### Academic Integrity
- **No Cheating:** All work has been done independently without unauthorized assistance.  
- **No Copying or Plagiarism:** This report and code are completely original.  
- **Proper Citation:** Concepts and equations are based on given assignment data and standard optimization methods.

---

## 🧮 Problem Statement

Find the unknown parameters **θ**, **M**, and **X** in the given **parametric equation** of a curve:
```python
x = t·cos(θ) − e^(M|t|)·sin(0.3t)·sin(θ) + X
y = 42 + t·sin(θ) + e^(M|t|)·sin(0.3t)·cos(θ)
```

### Unknowns and their ranges:
0° < θ < 50°

−0.05 < M < 0.05

0 < X < 100

### Parameter t range:
6 < t < 60

### Given:
A list of (x, y) points in **xy_data.csv** that lie on the curve.

---

## 🎯 Objective

Estimate the values of **θ**, **M**, and **X** such that the predicted curve fits the given data as accurately as possible.

## 🧠 Approach and Methodology

### Step 1 – Data Preparation
- The provided file `xy_data.csv` was read using **pandas**.  
- The variable `t` was generated uniformly between 6 and 60 if not already present.

### Step 2 – Model Function
Defined the parametric curve as functions of t, θ, M, and X:

```
x(t) = t·cos(θ) − e^(M|t|)·sin(0.3t)·sin(θ) + X
y(t) = 42 + t·sin(θ) + e^(M|t|)·sin(0.3t)·cos(θ)
```

### Step 3 – Objective Function
Used **L1 loss** to minimize absolute differences between predicted and true points:
Loss = Σ |x_pred − x_data| + |y_pred − y_data|

### Step 4 – Optimization
Used `scipy.optimize.minimize` with **L-BFGS-B** method and parameter bounds:
0° < θ < 50°, −0.05 < M < 0.05, 0 < X < 100


### Step 5 – Visualization
Generated a comparison plot:
- Blue dots → given data points  
- Red line → best-fit predicted curve  
Saved as **data_vs_model.png**

---

## 📊 Results

| Parameter | Symbol | Estimated Value | Range |
|------------|----------|-----------------|--------|
| Angle | θ | 0.4907 radians (≈ 28.11°) | 0° < θ < 50° |
| Exponential Factor | M | 0.0210 | −0.05 < M < 0.05 |
| Translation Constant | X | 54.90 | 0 < X < 100 |

**Final L1 Loss:** 37,865.12
---

## 🧩 Final Parametric Equation

Final estimated model:
```
x = t·cos(0.4907) − e^(0.0210|t|)·sin(0.3t)·sin(0.4907) + 54.9000
y = 42 + t·sin(0.4907) + e^(0.0210|t|)·sin(0.3t)·cos(0.4907)
```

## 💻 Code Used

The complete code is available in **fit_curve.py**.

Key libraries:-
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
```


