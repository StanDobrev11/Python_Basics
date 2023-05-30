h = int(input())
x = int(input())
y = int(input())

x_1 = 0
x_2 = 3 * h
y_1 = 0
y_2 = 1 * h

a_1 = 1 * h
a_2 = 2 * h
b_1 = h
b_2 = 4 * h

if a_1 <= x <= a_2 and b_1 <= y <= b_2:
    if x == a_1 or x == a_2 or y == b_1 or y == b_2:
        if y == h and a_1 < x < a_2:
            print("inside")
        else:
            print("border")
    else:
        print("inside")
elif x_1 <= x <= x_2 and y_1 <= y <= y_2:
    if x == x_1 or x == x_2 or y == y_1 or y == y_2:
        print("border")
    else:
        print("inside")

else:
    print("outside")
