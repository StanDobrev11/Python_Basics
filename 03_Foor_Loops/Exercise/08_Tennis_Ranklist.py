# •	Брой турнири, в които е участвал – цяло число в интервала [1…20]
# •	Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# •	Достигнат етап от турнира – текст – "W", "F" или "SF"

tournaments = int(input())
initial_score = int(input())

final_score = initial_score
win = 0
for _ in range(tournaments):
    stage_completed = input()
    if stage_completed == "W":
        final_score += 2000
        win += 1
    elif stage_completed == "F":
        final_score += 1200
    elif stage_completed == "SF":
        final_score += 720

print(f"Final points: {final_score}")
print(f"Average points: {int((final_score - initial_score) / tournaments)}")
print(f"{100 * win / tournaments :.2f}%")
