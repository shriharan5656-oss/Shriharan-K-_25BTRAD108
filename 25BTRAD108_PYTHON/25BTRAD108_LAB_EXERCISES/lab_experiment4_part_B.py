import math
def rectangle_area(length, width):
    return length * width
def circle_area(radius):
    return math.pi * radius * radius
print("AREA CALCULATOR")
print("1. Rectangle")
print("2. Circle")
option = int(input("Select shape: "))
if option == 1:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    result = rectangle_area(l, w)
    print(f"Rectangle area = {result:.2f}")
elif option == 2:
    r = float(input("Enter radius: "))
    result = circle_area(r)
    print(f"Circle area = {result:.2f}")
else:
    print("Invalid selection”)
