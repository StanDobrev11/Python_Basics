import math

bricks = int(input())
workers = int(input())
cart_capacity = int(input())

per_course = workers * cart_capacity
minimum_courses = bricks / per_course

print(math.ceil(minimum_courses))
