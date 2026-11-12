def is_even_or_odd(number):
    if type(number) is not int:
        return "unknown"

    if number % 2 == 0:
        return "even"
    else:
        return "odd"


def count_even(is_even_or_odd, n):
    count = 0

    for i in range(n):
        if is_even_or_odd(i) == "even":
            count += 1

    return count


print(count_even(is_even_or_odd, 5))
print(count_even(is_even_or_odd, 10))
print(count_even(is_even_or_odd, 7))
print(count_even(is_even_or_odd, 0))