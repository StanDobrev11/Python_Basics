failed_tasks = int(input())

max_failed_tasks = failed_tasks
ttl_tasks = 0
ttl_score = 0
is_failed = False
last_task = ""
while True:
    task_name = input()
    if task_name == "Enough":
        print(f"Average score: {ttl_score / ttl_tasks :.2f}\n"
              f"Number of problems: {ttl_tasks}\n"
              f"Last problem: {last_task}")
        break
    task_score = int(input())
    if task_score <= 4:
        failed_tasks -= 1
        if failed_tasks == 0:
            is_failed = True
            break
    ttl_tasks += 1
    ttl_score += task_score
    last_task = task_name

if is_failed:
    print(f"You need a break, {max_failed_tasks} poor grades.")
