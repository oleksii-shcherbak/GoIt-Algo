import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Define the function to integrate
def f(x):
    return x ** 2

# Integration limits
a = 0
b = 2

# Compute true value with SciPy
true_result, true_error = spi.quad(f, a, b)

# Monte Carlo method
def monte_carlo_integrate(func, x_min, x_max, num_samples=100_000):
    x_rand = np.random.uniform(x_min, x_max, num_samples)
    y_rand = np.random.uniform(0, func(x_max), num_samples)

    under_curve = y_rand <= func(x_rand)

    rect_area = (x_max - x_min) * func(x_max)
    estimated_integral = rect_area * np.sum(under_curve) / num_samples

    return estimated_integral, x_rand[under_curve], y_rand[under_curve]

# Run Monte Carlo integration
estimated_result, x_inside, y_inside = monte_carlo_integrate(f, a, b)

# Print results
print(f"True integral value (quad): {true_result}")
print(f"Monte Carlo estimated value: {estimated_result}")

# Plotting
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2, label='f(x) = x²')

# Fill area under curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label='Area under curve')

# Plot points under the curve
ax.plot(x_inside, y_inside, '.', markersize=0.5, color='blue', label='Random points under f(x)')

# Axis config
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Integration of f(x) = x² from {a} to {b}')
ax.legend()
plt.grid(True)
plt.show()
