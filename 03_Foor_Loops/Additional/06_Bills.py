months = int(input())

ttl_electricity = 0
ttl_others = 0
water = 20
internet = 15
for _ in range(months):
    electricity = float(input())
    others = (electricity + water + internet) * 1.2
    ttl_electricity += electricity
    ttl_others += others

ttl = ttl_electricity + water * months + internet * months + ttl_others
print(f"Electricity: {ttl_electricity :.2f} lv\n"
      f"Water: {water * months :.2f} lv\n"
      f"Internet: {internet * months :.2f} lv\n"
      f"Other: {ttl_others :.2f} lv\n"
      f"Average: {ttl / months :.2f} lv")
