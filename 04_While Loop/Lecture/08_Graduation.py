student = input()
average_score = 0
grade = 1
is_failed = False
failed = 0
while grade < 13:
    grade_score = float(input())
    if grade_score < 4:
        failed += 1
        if failed == 2:
            is_failed = True
            break
        continue
    average_score += grade_score
    grade += 1

if not is_failed:
    print(f"{student} graduated. Average grade: {average_score / 12 :.2f}")
else:
    print(f"{student} has been excluded at {grade} grade")
