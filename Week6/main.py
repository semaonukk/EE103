from say_hello import say_my_name
from triangle_area import calc_area

my_name = "Alice"
returned_name = say_my_name(my_name)
print("Returned value:", returned_name)

side = 5

triangle_area = calc_area(side)
print("Returned area:", triangle_area)

from convertor import binary_convertor

number = 13
binary_representation = binary_convertor(number)
print("decimal:", number)
print("binary:", binary_representation)