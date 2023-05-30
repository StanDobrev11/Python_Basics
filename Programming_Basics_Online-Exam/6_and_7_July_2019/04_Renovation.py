height = int(input())
width = int(input())
not_painted = int(input())

total_area = 4 * height * width
no_paint = total_area * not_painted / 100
to_paint = round(total_area - no_paint)

is_tired = False
is_painted = False
painted = 0
while not is_tired and not is_painted:
    liters_or_tired = input()
    if liters_or_tired == "Tired!":
        is_tired = True
    else:
        liters = int(liters_or_tired)
        painted += liters
        if painted >= to_paint:
            is_painted = True

if is_tired:
    remaining = to_paint - painted
    print(f"{remaining} quadratic m left.")
elif is_painted:
    if painted > to_paint:
        remaining = to_paint - painted
        print(f"All walls are painted and you have {abs(remaining)} l paint left!")
    else:
        print("All walls are painted! Great job, Pesho!")
