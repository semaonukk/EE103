def binary_convertor(number):
    if number == 0:
        return "0"
    binary = ""
    n = number

    while n > 0:
        remainder = n %2
        binary = str(remainder) + binary
        n = n // 2
        
    return binary