from secret_number import secretNum
import time
attempts = 0


while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == secretNum:
        print(f" Congratulations! You guessed the secret number in {attempts} attempts.")
        break

    elif guess < secretNum:
        print("your guess is too low")
    else :
        print("your guess is too high")
    if attempts == 5:
        break
    

if guess != secretNum:
    while True:
        print("Oh ! Noooooo..")
        time.sleep(1)

        