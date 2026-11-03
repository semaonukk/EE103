from secret_data import secret_number

epsilon = 0.01
guess = secret_number / 2
num_guesses = 0

while abs(guess**2 - secret_number) >= epsilon:

    guess = guess - (guess**2 - secret_number) / (2 * guess)

    num_guesses += 1

print("Newton-Raphson Method")
print("Square root:", guess)
print("Number of guesses:", num_guesses)
print("Error:", abs(guess**2 - secret_number))