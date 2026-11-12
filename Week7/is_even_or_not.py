def is_even_or_odd(number):
    if type(number) != int:
        return "Input must be an integer"
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
print(is_even_or_odd(4))  # Output: even
print(is_even_or_odd(5))  # Output: odd
print(is_even_or_odd("hello"))  # Output: Input must be an integer
print(is_even_or_odd(8.00))
print(is_even_or_odd("7"))  # Output: odd