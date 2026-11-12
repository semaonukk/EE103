def count_evens(input_n):
    count = 0

    for num in range(input_n):

        import pdb
        pdb.set_trace()

        if num % 2 == 0:
            count += 1

    return count


print("Total evens:", count_evens(5))