n = int(input("Enter a number you want to find factorial of: "))
factorial = 1
i = 1

if n < 0:
    print("Factorial is not defined for negative numbers.") 
else:
    while i <= n:
        factorial *= i
        i+= 1
    print(f"The factorial of {n} is: {factorial}")
    