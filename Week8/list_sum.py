total = 0
dummy_range = range(10)

dummy_list_1 = list(dummy_range)

dummy_list_2 = []

for number in dummy_range:
    dummy_list_2.append(number)

print("List 1:", dummy_list_1) 
print("List 2:", dummy_list_2)
print("Are they equal?:", dummy_list_1== dummy_list_2)

for number in dummy_list_1:
    total += number

print("Total:", total)

