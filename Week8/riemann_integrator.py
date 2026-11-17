def integrate(func, steps=1000):

    total_area = 0
    dx = 1 / steps

    for i in range(steps):
        x = (i + 0.5) * dx
        area = func(x) * dx
        total_area += area

    return total_area

def take_square(x):
    return x**2

result = integrate(take_square)

print("Estimated integral:", result)  

print(integrate(lambda x: x**2))
print(integrate(lambda x: x))
print(integrate(lambda x: 1))