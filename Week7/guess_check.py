
number = float(input("Enter a number to find its cube root: "))

guess = 0.0
step = 0.001
epsilon = 0.01

while abs(guess ** 3 - number) >= epsilon and guess <= number:
    print(f"Current guess: {guess}, Current guess cubed: {guess ** 3}")
    guess += step

print(f"Cube root of {number} is approximately {guess}")