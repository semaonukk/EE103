x = float(input("what x to find the cube root of? "))
g = float(input("what is your guess? "))

if g == 0:
    print("Your guess cannot be zero.")
else:
    print("current estimate cubed:", g**3)
    next_guess = g - ((g**3 - x) / (3 * g**2))
    print("next guess:", next_guess)
