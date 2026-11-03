from secret_data import secret_year

low = 0
high = 2026
num_guesses = 1

guess = (high + low) // 2

while guess != secret_year:
    print("Current guess:", guess)
    num_guesses += 1

    if guess < secret_year:
        low = guess + 1
    else:
        high = guess - 1

    guess = (high + low) // 2

print("secret year found:", guess)
print("number of guesses:", num_guesses)