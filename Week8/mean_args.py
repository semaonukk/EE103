def mean(*args):
    tot = 0

    for number in args:
        tot += float(number)

    return tot / len(args)

print(mean(4,6,8))
print(mean(1,2,"3",4,5))