students = int(input())

fail = 0
average = 0
mid = 0
good = 0
best = 0
average_grade = 0
for _ in range(students):
    student_grade = float(input())
    if 2 <= student_grade < 3:
        fail += 1
    elif student_grade < 4:
        average += 1
    elif student_grade < 5:
        good += 1
    else:
        best += 1
    average_grade += student_grade
print(f"Top students: {100 * best / students :.2f}%")
print(f"Between 4.00 and 4.99: {100 * good / students :.2f}%")
print(f"Between 3.00 and 3.99: {100 * average / students :.2f}%")
print(f"Fail: {100 * fail / students :.2f}%")
print(f"Average: {average_grade / students :.2f}")
