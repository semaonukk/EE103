def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

def calculator(operation, x, y):
    return operation(x, y)

print("Addition:")
print(add(3, 5))
print(calculator(add, 3, 5))

print("Subtraction:")
print(subtract(3, 5))
print(calculator(subtract, 3, 5))

print("Multiplication:")
print(multiply(3, 5))
print(calculator(multiply, 3, 5))

print("Division:")
print(divide(3, 5))
print(calculator(divide, 3, 5))