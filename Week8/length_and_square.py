def length_and_square(L):
    length = len(L)

    squares = []

    for number in L:
        squares.append(number**2)

    return length, squares


result = length_and_square([1, 3, 5])

print(result)