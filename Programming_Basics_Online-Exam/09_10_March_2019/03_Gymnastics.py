country = input()
discipline = input()

difficulty = 0
performance = 0
MAX_SCORE = 20
if country == "Russia":
    if discipline == "ribbon":
        difficulty = 9.1
        performance = 9.4
        score = difficulty + performance
    elif discipline == "hoop":
        difficulty = 9.3
        performance = 9.8
        score = difficulty + performance
    else:
        difficulty = 9.6
        performance = 9.0
        score = difficulty + performance
if country == "Bulgaria":
    if discipline == "ribbon":
        difficulty = 9.6
        performance = 9.4
        score = difficulty + performance
    elif discipline == "hoop":
        difficulty = 9.55
        performance = 9.75
        score = difficulty + performance
    else:
        difficulty = 9.5
        performance = 9.4
        score = difficulty + performance
if country == "Italy":
    if discipline == "ribbon":
        difficulty = 9.2
        performance = 9.5
        score = difficulty + performance
    elif discipline == "hoop":
        difficulty = 9.45
        performance = 9.35
        score = difficulty + performance
    else:
        difficulty = 9.7
        performance = 9.15
        score = difficulty + performance

percent_not_enough = ((MAX_SCORE - score) / MAX_SCORE) * 100
print(f"The team of {country} get {score:.3f} on {discipline}.")
print(f"{percent_not_enough:.2f}%")

