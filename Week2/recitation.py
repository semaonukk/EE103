x = int(input("Enter a number you want to find factorial of: "))
factorial = 1
for i in range(1, x + 1,1):
    factorial *= i
print(f"The factorial of {x} is: {factorial}")