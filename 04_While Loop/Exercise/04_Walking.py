target_steps = 10_000

steps_to_home = 0
daily_steps = 0
is_going_home = False

while not is_going_home:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        is_going_home = True
    else:
        steps = int(command)
        daily_steps += steps
        if daily_steps >= target_steps:
            break

if not is_going_home:
    print(f"Goal reached! Good job!\n"
          f"{daily_steps - target_steps} steps over the goal!")
else:
    daily_steps += steps_to_home
    if daily_steps >= target_steps:
        print(f"Goal reached! Good job!\n"
              f"{daily_steps - target_steps} steps over the goal!")
    else:
        print(f"{target_steps - daily_steps} more steps to reach goal.")

