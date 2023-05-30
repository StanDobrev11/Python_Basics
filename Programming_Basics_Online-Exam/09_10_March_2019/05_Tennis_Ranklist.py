tournaments = int(input())
initial_points = int(input())

WINNER = 2000  # W
FINALIST = 1200  # F
SEMI_FINALIST = 720  # SF
current_points = 0
won = 0
for tournament in range(tournaments):
    tournament_current_stage = input()
    if tournament_current_stage == "W":
        current_points = current_points + WINNER
        won += 1
    if tournament_current_stage == "F":
        current_points = current_points + FINALIST
    if tournament_current_stage == "SF":
        current_points = current_points + SEMI_FINALIST

final_points = initial_points + current_points
average_per_tournament = current_points / tournaments
percent_tournaments_won = (won / tournaments) * 100
print(f"Final points: {final_points}")
print(f"Average points: {int(average_per_tournament)}")
print(f"{percent_tournaments_won:.2f}%")

