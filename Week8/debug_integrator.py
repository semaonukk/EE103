import pdb
def integrate(func, steps=1000):
    total_area = 0
    dx = 1 / steps

    for i in range(steps):
        x = (i+0.5) * dx
        area = func(x) * dx

        print("i =",i)
        print("x =",x)
        print("area =", area)
        print("total before= ",total_area)
        #pdb.set_trace()
        total_area += area

        print("total after =", total_area)
        print("---------------")

    return total_area

print("Result:", integrate(lambda x: x**2,4))