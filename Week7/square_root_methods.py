epsilon = 0.0001
step = 0.001
guess = 0.0
num_guesses = 0
number = float(input("Enter a number to find its square root: "))

while abs(guess **2 - number) >= epsilon and guess**2 < number:
    guess += step
    num_guesses += 1

if abs(guess ** 2 - number) < epsilon:
    print("Approximation :",guess)
    print("Number of guesses:", num_guesses)
else:
    print("Failed to find the square root of", number)

