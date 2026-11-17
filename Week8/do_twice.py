from math import sqrt

def f_x_twice(x, f_x):
    return f_x(f_x(x))

result = f_x_twice(16, sqrt)

print("square root twice:", result)  

result_lambda = f_x_twice(2, lambda x: x**2)
print("square twice:", result_lambda)