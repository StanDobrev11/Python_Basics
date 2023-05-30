musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_climbers = 0
groups = int(input())
for _ in range(groups):
    climbers_in_group = int(input())
    if climbers_in_group <= 5:
        musala += climbers_in_group
    elif climbers_in_group <= 12:
        monblan += climbers_in_group
    elif climbers_in_group <= 25:
        kilimanjaro += climbers_in_group
    elif climbers_in_group <= 40:
        k2 += climbers_in_group
    else:
        everest += climbers_in_group
    total_climbers += climbers_in_group

musala_percent = 100 * musala / total_climbers
monblan_percent = 100 * monblan / total_climbers
kilimanjaro_percent = 100 * kilimanjaro / total_climbers
k2_percent = 100 * k2 / total_climbers
everest_percent = 100 * everest / total_climbers

print(f"{musala_percent :.2f}%\n"
      f"{monblan_percent :.2f}%\n"
      f"{kilimanjaro_percent :.2f}%\n"
      f"{k2_percent :.2f}%\n"
      f"{everest_percent :.2f}%")
