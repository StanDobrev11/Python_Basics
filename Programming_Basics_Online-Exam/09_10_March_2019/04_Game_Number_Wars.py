player_one = input()
player_two = input()

is_playing = True
player_one_score = 0
player_two_score = 0
winner = ""
winner_score = 0
while is_playing:
    player_one_card = input()
    if player_one_card == "End of game":
        print(f"{player_one} has {player_one_score} points\n"
              f"{player_two} has {player_two_score} points")
        break
    else:
        player_one_card = int(player_one_card)
    player_two_card = input()
    if player_two_card == "End of game":
        print(f"{player_one} has {player_one_score} points\n"
              f"{player_two} has {player_two_score} points")
        break
    else:
        player_two_card = int(player_two_card)

    if player_one_card > player_two_card:
        score = player_one_card - player_two_card
        player_one_score = player_one_score + score
    elif player_two_card > player_one_card:
        score = player_two_card - player_one_card
        player_two_score = player_two_score + score
    elif player_one_card == player_two_card:
        print("Number wars!")
        player_one_card = int(input())
        player_two_card = int(input())
        if player_one_card > player_two_card:
            winner = player_one
            winner_score = player_one_score
        elif player_two_card > player_one_card:
            winner = player_two
            winner_score = player_two_score
        print(f"{winner} is winner with {winner_score} points")
        is_playing = False
    else:
        print(f"{player_one} has {player_one_score} points\n"
              f"{player_two} has {player_two_score} points")
        is_playing = False
