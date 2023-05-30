judges_count = int(input())

command = input()
count = 0
ttl_average = 0
while not command == "Finish":
    subject = command
    count += 1
    ttl_score = 0
    for _ in range(judges_count):
        score = float(input())
        ttl_score += score
    average_score = ttl_score / judges_count
    ttl_average += average_score
    print(f"{subject} - {average_score:.2f}.")
    command = input()

ttl_average /= count
print(f"Student's final assessment is {ttl_average:.2f}.")
