# Monte Carlo Integration

## Overview
This project demonstrates the use of the Monte Carlo method to calculate the integral of a function, as well as comparing the result with an analytical solution. Specifically, we integrate the function `f(x) = x^2` over the interval from 0 to 2 using the Monte Carlo approach and compare it with the result from the `quad` function of the SciPy library.

## Monte Carlo Method
The Monte Carlo method is a statistical technique that uses random sampling to estimate numerical results. In this case, we use it to estimate the value of the definite integral of the function `f(x) = x^2` over the interval `[0, 2]`. The key idea is to generate random points within the interval and calculate the average value of the function to approximate the area under the curve.

### Steps:
1. Generate `N` random points in the interval `[a, b]`.
2. Evaluate the function at these random points.
3. Compute the mean value of the function and multiply it by the width of the interval `(b - a)` to estimate the integral.

### Result:
For `N = 10000` random points, the Monte Carlo estimate for the integral was calculated and compared to the analytical solution obtained using the `quad` function.

## Analytical Method
The `quad` function from the SciPy library was used to obtain the exact value of the integral. This method provides a highly accurate result and also returns an estimate of the absolute error.

### Results:
- **Monte Carlo Integral**: The estimated value of the integral using the Monte Carlo method.
- **Analytical Integral**: The exact value calculated using the `quad` function.
- **Absolute Error**: The absolute difference between the Monte Carlo estimate and the analytical result.

## Conclusion
The Monte Carlo method provides a good approximation of the integral, with accuracy depending on the number of random samples (`N`). In this case, with `N = 10000`, the result was close to the analytical solution, demonstrating the effectiveness of the Monte Carlo approach for numerical integration.

However, it is important to note that the Monte Carlo method introduces randomness, and its accuracy improves as the number of samples increases. In contrast, the analytical method (`quad`) provides an exact solution with a known error bound. Therefore, the Monte Carlo method is useful in scenarios where an exact solution is difficult or impossible to obtain, while the analytical approach is preferable when it is computationally feasible and provides higher accuracy.

