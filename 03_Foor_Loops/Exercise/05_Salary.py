tabs_open = int(input())
salary = int(input())

tabs_dict = {"Facebook": 150, "Instagram": 100, "Reddit": 50}
for _ in range(tabs_open):
    website = input()
    if website in tabs_dict:
        salary -= tabs_dict[website]
    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(salary)
