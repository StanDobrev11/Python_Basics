from math import pi, pow

type_of_figure = input()

if type_of_figure == "square":
    side = float(input())
    area = pow(side, 2)
elif type_of_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif type_of_figure == "circle":
    radius = float(input())
    area = pi * pow(radius, 2)
else:   # if triangle
    side = float(input())
    height = float(input())
    area = side * height / 2

print(f"{area:.3f}")
