import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Define the function and integration limits
def f(x):
    return x ** 2

a = 0  # Lower limit
b = 2  # Upper limit

# Monte Carlo method for calculating the integral
N = 10000  # Number of random points
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)

# Calculate the mean value of the function and the area under the curve
mean_value = np.mean(y_rand)
monte_carlo_integral = mean_value * (b - a)

# Analytical calculation of the integral using quad
result, error = spi.quad(f, a, b)

# Compare the results
print("Monte Carlo Integral:", monte_carlo_integral)
print("Analytical Integral:", result)
print("Absolute Error of Monte Carlo Method:", abs(result - monte_carlo_integral))

# Create a range of values for x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Create the plot
fig, ax = plt.subplots()

# Plot the function
ax.plot(x, y, 'r', linewidth=2)

# Fill the area under the curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Configure the plot
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Add integration limits and title
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Integration Plot of f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()