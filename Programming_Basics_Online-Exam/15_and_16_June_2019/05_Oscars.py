actor_name = input()
academy_initial_points = float(input())
judges = int(input())

TARGET_SCORE = 1250.5
actor_score = academy_initial_points
for each_judge in range(judges):
    judge_name = input()
    judge_score = float(input())
    actor_score += len(judge_name) * judge_score / 2
    if actor_score > TARGET_SCORE:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_score:.1f}!")
        break

if actor_score < TARGET_SCORE:
    required_score = TARGET_SCORE - actor_score
    print(f"Sorry, {actor_name} you need {required_score:.1f} more!")
