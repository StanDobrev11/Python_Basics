actor = input()
initial_points = float(input())
judges = int(input())
total_points = initial_points
for _ in range(judges):
    judge = input()
    judge_score = float(input())
    total_points += len(judge) * judge_score / 2
    if total_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points :.1f}!")
        break
else:
    print(f"Sorry, {actor} you need {1250.5 - total_points :.1f} more!")
