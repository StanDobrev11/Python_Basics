students = int(input())

fail_count = 0
av_count = 0
good_count = 0
top_count = 0
grades = 0
for _ in range(students):
    grade = float(input())
    if grade < 3:
        fail_count += 1
    elif grade < 4:
        av_count += 1
    elif grade < 5:
        good_count += 1
    else:
        top_count += 1
    grades += grade

percent_fail = 100 * fail_count / students
percent_average = 100 * av_count / students
percent_good = 100 * good_count / students
percent_top = 100 * top_count / students
av_grades = grades / students

print(f"Top students: {percent_top:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good:.2f}%")
print(f"Between 3.00 and 3.99: {percent_average:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {av_grades:.2f}")
