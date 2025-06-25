# Task 2 — Definite Integral Using Monte Carlo

## 🎯 Goal

Estimate the definite integral of the function `f(x) = x²` over the interval `[0, 2]` using the **Monte Carlo method**.  
Compare the result with the analytical solution calculated using SciPy’s `quad` function.

---

## 📐 Analytical Result

The exact integral of `f(x) = x²` over `[0, 2]` is:

∫₀² x² dx = 8⁄3 ≈ **2.6667**

Using SciPy:
```python
from scipy.integrate import quad

def f(x):
    return x ** 2

result, error = quad(f, 0, 2)
```

**Result:** 2.6667  
**Error:** ~2.96e-14

---

## 🎲 Monte Carlo Approximation

Using 100,000 random points to estimate the integral:

**Estimated result:** ~2.66 (varies slightly each run)

---

## 📊 Comparison

| Method       | Result   | Error            |
|--------------|----------|------------------|
| SciPy `quad` | 2.6667   | ≈ 0              |
| Monte Carlo  | ~2.66    | ~0.002 – 0.005   |

---

## ✅ Conclusion

The Monte Carlo method provides an approximate result close to the analytical one. However, it is subject to statistical error and requires many iterations to improve accuracy.  
For well-behaved functions like `x²`, deterministic methods such as SciPy’s `quad` are more efficient and precise.
