import math

def calc_area(side_length):
    
    area = (math.sqrt(3) / 4) * (side_length ** 2)
    print("Area of the triangle with side length", side_length, "is:", area)
    return area
