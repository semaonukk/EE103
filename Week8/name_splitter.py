def name_splitter(full_name):
    parts = full_name.split()

    first_name = " ".join(parts[:-1])
    surname = parts[-1]

    return first_name, surname

result = name_splitter("Ada Lovelace")

print(result)
print(type(result))