budget_for_actors = float(input())

budget_remaining = budget_for_actors
salary = 0
while True:
    actor_name = input()
    if actor_name == "ACTION" or budget_remaining <= 0:
        break
    elif len(actor_name) <= 15:
        salary = float(input())
    elif len(actor_name) > 15:
        salary = budget_remaining * 0.2

    budget_remaining -= salary

if budget_remaining >= 0:
    print(f"We are left with {budget_remaining:.2f} leva.")
else:
    print(f"We need {abs(budget_remaining):.2f} leva for our actors.")