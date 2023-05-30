best_score = 0
best_player = ""
while True:
    player_name = input()
    if player_name == "END":
        break
    goals_scored = int(input())
    if goals_scored > best_score:
        best_score = goals_scored
        best_player = player_name
    if goals_scored >= 10:
        break

if best_score >= 3:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
else:
    print(f"{best_player} is the best player!")
    print(f"He has scored {best_score} goals.")
