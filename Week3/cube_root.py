given_number = int(input("Enter an integer: "))

target = abs(given_number)
guess = 0

while guess**3 < target:
    guess += 1

if guess**3 == target:
    if given_number < 0:
        guess = -guess

    print(f"The cube root of {given_number} is {guess}")

else:
    low = guess - 1
    high = guess

    while high - low > 0.000001:
        middle = (low + high) / 2

        if middle**3 < target:
            low = middle
        else:
            high = middle

    cube_root = (low + high) / 2

    if given_number < 0:
        cube_root = -cube_root

    print(f"The approximate cube root is {cube_root:.6f}")