import math

n1 = 1
n2 = 2
n3 = 3

count = 0
print(n1, n2, n3, end=" ")
while count < 20:
    nnext = n1 + n2 + n3
    n1 = n2
    n2 = n3
    n3 = nnext
    print(nnext, end=" ")
    count += 1

matrix_start = 5
matrix_step = 2
print()
new_count = 0
while new_count < 20:
    space_count = math.ceil(new_count / 2)
    matrix_start += matrix_step * space_count
    print(matrix_start, end=" ")
    new_count += 1

