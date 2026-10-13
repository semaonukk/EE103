n = int(input(" enter a positive integer: "))

if n < 1:
    print("Please enter a positive integer.")

else:
    running_sum = 0

    for i in range(1, n + 1):
        running_sum += i

    sum_gauss = n * (n + 1) // 2

    print("Running sum:", running_sum)
    print("Gauss sum:", sum_gauss)

    if running_sum == sum_gauss:
        print("My running sum code works correctly")
    else:
        print("My running sum code failed badly")