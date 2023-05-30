import math

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

matrix_start = int(input())
matrix_step = int(input())
next_num = 0
factor = 0
while next_num != matrix_start:
    if matrix_start == num_1 or matrix_start == num_2 or matrix_start == num_3:
        print(matrix_start)
        break

    if matrix_start > 1_000_000 or next_num > 1_000_000:
        print("No")
        break

    if next_num > matrix_start:  # nums in spiral
        space_count = math.ceil(factor / 2)
        matrix_start += matrix_step * space_count
        factor += 1
    elif next_num < matrix_start:  # tribonacci
        next_num = num_1 + num_2 + num_3
        num_1 = num_2
        num_2 = num_3
        num_3 = next_num

if next_num == matrix_start:
    print(matrix_start)
