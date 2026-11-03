from secret_data import secret_year

epsilon = 0.01
step = 0.00001
guess = 0.0
num_guesses = 0

while abs(guess**2 - secret_year) >= epsilon and guess <= secret_year:
    guess += step
    num_guesses += 1

print("Approximation Method:")
print("Number of guesses:", num_guesses)
print("square root approximation:", guess)
print("Error:", abs(guess**2 - secret_year))