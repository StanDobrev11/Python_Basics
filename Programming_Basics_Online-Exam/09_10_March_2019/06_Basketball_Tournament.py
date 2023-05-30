tournament_name = ""
games_won = 0
games_lost = 0
total_games = 0
while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break
    games_in_tournament = int(input())
    games_count = 0
    total_games += games_in_tournament
    for game in range(games_in_tournament):
        games_count += 1
        points_for = int(input())
        points_against = int(input())
        if points_for > points_against:
            points_diff = points_for - points_against
            games_won += 1
            print(f"Game {games_count} of tournament "
                  f"{tournament_name}: win with {points_diff} points.")
        else:
            points_diff = points_against - points_for
            games_lost += 1
            print(f"Game {games_count} of tournament "
                  f"{tournament_name}: lost with {points_diff} points.")

percent_won = (games_won / total_games) * 100
percent_lost = 100 - percent_won

print(f"{percent_won:.2f}% matches win\n"
      f"{percent_lost:.2f}% matches lost")
