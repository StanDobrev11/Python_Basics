working_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekends = ("Saturday", "Sunday")
fruit_list = ("banana",
              "apple",
              "orange",
              "grapefruit",
              "kiwi",
              "pineapple",
              "grapes")
work_days_price = {"banana": 2.5,
                   "apple": 1.2,
                   "orange": 0.85,
                   "grapefruit": 1.45,
                   "kiwi": 2.7,
                   "pineapple": 5.5,
                   "grapes": 3.85}
weekend_price = {"banana": 2.7,
                 "apple": 1.25,
                 "orange": 0.9,
                 "grapefruit": 1.6,
                 "kiwi": 3,
                 "pineapple": 5.6,
                 "grapes": 4.2}

fruit = input()
day = input()
qtity = float(input())

cost = 0
if day in working_days:
    if fruit not in fruit_list:
        print("error")
    else:
        cost = qtity * work_days_price[fruit]
        print(f"{cost:.2f}")
elif day in weekends:
    if fruit not in fruit_list:
        print("error")
    else:
        cost = qtity * weekend_price[fruit]
        print(f"{cost:.2f}")
else:
    print("error")
