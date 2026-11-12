def sqrt_guess_and_check(n):
    for guess in range(n + 1):
        if guess ** 2 == n:
            return guess
    return None


def sqrt_approximation(n):

    epsilon = 0.01
    step = 0.001
    guess = 0.0

    while abs(guess ** 2 - n) >= epsilon and guess <= n:
        guess += step

    if abs(guess ** 2 - n) < epsilon:
        return guess
    
    return None

def sqrt_bisection_search(n):
    epsilon = 0.01
    low = 0.0
    high = max(1.0, n)
    guess = (low + high) / 2.0

    while abs(guess ** 2 - n) >= epsilon:
        if guess ** 2 < n:
            low = guess
        else:
            high = guess

        guess = (low + high) / 2.0

    return guess

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    print("Guess and Check:", sqrt_guess_and_check(number))
    print("Approximation:", sqrt_approximation(number))
    print("Bisection Search:", sqrt_bisection_search(number))