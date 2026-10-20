import math
x=0
for i in range(10):
    x += 0.1

print("Results :", x)
print("Exact equality:", x == 1.0)
print("Difference:", abs(x - 1.0))
print("Approximately equal:", math.isclose(x, 1.0))
print(f"Formatted result: {x:.2f}")
