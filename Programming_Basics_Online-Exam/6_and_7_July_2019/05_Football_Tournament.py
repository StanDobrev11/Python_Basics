football_team = input()
games_played = int(input())

win = 0
lost = 0
draw = 0
for game in range(games_played):
    result = input()
    if result == "W":
        win += 1
    elif result == "L":
        lost += 1
    else:
        draw += 1

points = win * 3 + draw

if games_played == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    percent_wins = 100 * (win / games_played)
    print(f"{football_team} has won {points} points during this season.\n"
          f"Total stats:\n"
          f"## W: {win}\n"
          f"## D: {draw}\n"
          f"## L: {lost}\n"
          f"Win rate: {percent_wins:.2f}%")
