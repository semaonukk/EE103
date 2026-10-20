original = float(input("Enter a decimal fraction (0 <= F < 1): "))

fraction = original
binary = ""
result = 0.0

epsilon = 0.0001
position = 1
max_digits = 64

if original < 0 or original >= 1:
    print("Please enter a number between 0 and 1.")

else:
    while (abs(result - original) >= epsilon
           and fraction != 0
           and position <= max_digits):

        fraction *= 2

        bit = int(fraction)

        binary += str(bit)

        result += bit / (2 ** position)

        fraction -= bit

        position += 1

    if binary == "":
        binary = "0"

    print("Binary:", "0." + binary)
    print("Approximate decimal:", result)
    print("Absolute error:", abs(result - original))