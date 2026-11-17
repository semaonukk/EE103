def estimate_derivative(f, x, h=1e-5):

    derivative = (f(x+h) - f(x-h)) / (2*h)
    return derivative

def square(x):
    return x**2

result = estimate_derivative(square, 5)
print("Estimated derivative of square at x=5:", result)  # Output: Estimated derivative of square at x=5: 10.000000000013102
print("Exact derivative of square at x=5:", 2*5)  # Output: Exact derivative of square at x=5: 10

square_lambda = lambda x: x**2

result_lambda = estimate_derivative(square_lambda, 5)

print("Lambda derivative:", result_lambda)
