year_type = input()
holidays = int(input())
weekends_not_in_Sofia = int(input())

WEEKENDS_IN_YEAR = 48
WEEKENDS_PLAYING = (WEEKENDS_IN_YEAR - weekends_not_in_Sofia) * 3 / 4
HOLIDAYS_PLAYING = holidays * 2 / 3
LEAP_YEAR = 0.15  # percent more volleyball

playing_volleyball = HOLIDAYS_PLAYING + WEEKENDS_PLAYING + weekends_not_in_Sofia

if year_type == "leap":
    playing_volleyball = playing_volleyball + playing_volleyball * LEAP_YEAR

print(int(playing_volleyball))
