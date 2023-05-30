day_of_week = input()

working_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

if day_of_week == "Saturday" or day_of_week == "Sunday":
    print("Weekend")

elif day_of_week in working_days:
    print("Working day")

else:
    print("Error")
   