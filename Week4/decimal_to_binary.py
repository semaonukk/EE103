num = int(input("Enter a non-negative decimal integer: "))

original_num = num

if num < 0:
    print("Please enter a non-negative integer.")

elif num == 0:
    print("0 converted to binary is 0")

else:
    remainders = ""

    while num > 0:
        remainder = num % 2
        remainders += str(remainder)
        num = num // 2

    binary = remainders[::-1]

    print(f"{original_num} converted to binary is {binary}")