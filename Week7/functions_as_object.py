def is_even_or_odd(number):
    if type(number) is not int:
        return "unknown"

    if number % 2 == 0:
        return "even"
    else:
        return "odd"


is_even_or_odd_alias = is_even_or_odd

print(is_even_or_odd(8))
print(is_even_or_odd_alias(8))

print(is_even_or_odd(7))
print(is_even_or_odd_alias(7))

print(is_even_or_odd(8.0))
print(is_even_or_odd_alias(8.0))