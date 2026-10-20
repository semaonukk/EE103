import time

start = time.perf_counter()

for alyssa in range(1001):

    ben = alyssa - 20
    cindy = 2 * alyssa

    if (ben >= 0 and
        alyssa + ben + cindy == 1000):

        solution = (alyssa, ben, cindy)

end = time.perf_counter()

print("Solution:", solution)
print(f"Elapsed time: {end - start:.6f} seconds")