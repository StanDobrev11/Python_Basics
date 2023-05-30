group_count = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_climbers = 0
for group in range(group_count):
    members_per_group = int(input())
    if members_per_group >= 41:
        everest += members_per_group
    elif members_per_group >= 26:
        k2 += members_per_group
    elif members_per_group >= 13:
        kilimanjaro += members_per_group
    elif members_per_group >= 6:
        monblan += members_per_group
    else:
        musala += members_per_group
    total_climbers += members_per_group

percent_musala = 100 * (musala / total_climbers)
percent_monblan = 100 * (monblan / total_climbers)
percent_kilimanjaro = 100 * (kilimanjaro / total_climbers)
percent_k2 = 100 * (k2 / total_climbers)
percent_everest = 100 * (everest / total_climbers)

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
