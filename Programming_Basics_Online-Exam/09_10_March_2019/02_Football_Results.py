home_team = 0
away_team = 0
draw = 0

for game in range(3):
    game = input()
    if int(game[0]) > int(game[2]):
        home_team += 1
    elif int(game[0]) < int(game[2]):
        away_team += 1
    else:
        draw += 1

print(f"Team won {home_team} games.")
print(f"Team lost {away_team} games.")
print(f"Drawn games: {draw}")

