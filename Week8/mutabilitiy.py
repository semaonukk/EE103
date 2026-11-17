my_list = [1, 3, 5]
my_tuple = (1, 3, 5)

# Lists are mutable
my_list[1] = 5
print("Modified list:", my_list)

# Tuples are immutable
try:
    my_tuple[1] = 5
except TypeError as error:
    print("Tuple error:", error)

print("Original tuple:", my_tuple)