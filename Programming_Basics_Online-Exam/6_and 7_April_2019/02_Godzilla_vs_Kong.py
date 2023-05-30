movie_budget = float(input())
statists = int(input())
statist_costume_price = float(input())

movie_decor = movie_budget * 0.1
if statists > 150:
    statist_costume_price -= statist_costume_price * 0.1

movie_cost = movie_decor + statist_costume_price * statists
money_needed = movie_cost - movie_budget
money_left = movie_budget - movie_cost

if movie_cost > movie_budget:
    print(f"Not enough money!\n"
          f"Wingard needs {money_needed:.2f} leva more.")
else:
    print(f"Action!\n"
          f"Wingard starts filming with {money_left:.2f} leva left.")

