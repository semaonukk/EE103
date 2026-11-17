def char_counts(s):
    vowels = 0
    consonants = 0

    for char in s:
        if char in "aeiou" :
            vowels += 1
        elif char.isalpha():
            consonants += 1

    return (vowels, consonants)

print(char_counts("hello"))
print(char_counts("programming"))
