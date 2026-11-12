def calculator(operation, x, y):
    return operation(x, y)

add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b

print("Addition:", calculator(add, 3, 5))
print("Subtraction:", calculator(subtract, 3, 5))
print("Multiplication:", calculator(multiply, 3, 5))
print("Division:", calculator(divide, 3, 5))