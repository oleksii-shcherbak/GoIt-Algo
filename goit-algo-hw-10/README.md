# Task 2 — Definite Integral Using Monte Carlo

## Goal
Calculate the definite integral of $begin:math:text$ f(x) = x^2 $end:math:text$ over [0, 2] using the Monte Carlo method. Compare the result with SciPy’s `quad` function and provide conclusions.

---

## Analytical Result

$begin:math:display$
\\int_0^2 x^2 dx = \\frac{8}{3} \\approx 2.6667
$end:math:display$

Using SciPy:
```python
result, error = quad(f, 0, 2)
```
**Result:** 2.6667  
**Error:** ~2.96e-14

---

## Monte Carlo Approximation

Using 100,000 random points:  
**Estimated result:** ~2.66 (varies slightly each run)

---

## Comparison

| Method      | Result   | Error     |
|-------------|----------|-----------|
| SciPy `quad`| 2.6667   | ~0        |
| Monte Carlo | ~2.66    | ~0.002–0.005 |

---

## Conclusion

- Monte Carlo gives a good approximation, especially with many points.
- SciPy `quad` is more accurate for 1D integrals.
- Monte Carlo is more useful for complex or multi-dimensional cases.

---
