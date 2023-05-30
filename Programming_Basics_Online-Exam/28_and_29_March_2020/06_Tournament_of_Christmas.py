days_of_tournament = int(input())
WIN = 20

daily_cash = 0
tournament_cash = 0
days_won = 0
for each in range(days_of_tournament):
    game_cash = 0
    won = 0
    lost = 0
    while True:
        sport = input()
        if sport == "Finish":
            if won > lost:
                game_cash = game_cash + game_cash * 0.1
                daily_cash += game_cash
                days_won += 1
            else:
                daily_cash += game_cash
            tournament_cash = daily_cash
            break
        win_or_lose = input()
        if win_or_lose == "win":
            won += 1
            game_cash += WIN
        else:
            lost += 1

days_lost = days_of_tournament - days_won
if days_won >= days_lost:
    tournament_cash = tournament_cash + tournament_cash * 0.2
    print(f"You won the tournament! Total raised money: {tournament_cash:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {tournament_cash:.2f}")
