from secret_data import secret_year

guess = 0
num_guesses = 0

while guess <= 2026:
    num_guesses += 1

    if guess == secret_year:
        print("secret year found:", guess)
        print("number of guesses:", num_guesses)
        break

    guess +=1