guest_count = int(input())
guest_voucher_price = float(input())
budget = float(input())

discount = 0
cake_price = budget * 10 / 100
if 10 <= guest_count <= 15:
  discount = 15 / 100
elif 16 <= guest_count <= 20:
  discount = 20 / 100
elif guest_count > 20:
  discount = 25 / 100

cash_needed = guest_count * (guest_voucher_price - guest_voucher_price * discount) + cake_price
cash_left = budget - cash_needed

if cash_left >= 0:
  print(f"It is party time! {cash_left:.2f} leva left.")
else:
  cash_left = cash_left * -1 +0
  print(f"No party! {cash_left:.2f} leva needed.")