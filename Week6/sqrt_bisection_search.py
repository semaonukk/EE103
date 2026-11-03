from secret_data import secret_year

epsilon = 0.01
low = 0.0
high = max(1.0, secret_year)
guess = (low + high) / 2.0
num_guesses = 1

while abs(guess**2 - secret_year) >= epsilon:
    if guess**2 < secret_year:
        low = guess
    else:
        high = guess

    guess = (low + high) / 2.0
    num_guesses += 1

print("Bisection Search Method:")
print("Square root approximation:", guess)
print("Number of guesses:", num_guesses)
print("Error:", abs(guess**2 - secret_year))