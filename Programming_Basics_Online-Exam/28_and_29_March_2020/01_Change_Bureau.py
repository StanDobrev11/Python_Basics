BITCOIN_TO_BGN = 1168
CYN_TO_USD = 0.15
USD_TO_BGN = 1.76
EUR_TO_BGN = 1.95

ttl_bitcoins = float(input())
ttl_cny = float(input())
commission = float(input())

ttl_bgn = ttl_bitcoins * BITCOIN_TO_BGN + ttl_cny * CYN_TO_USD * USD_TO_BGN
ttl_euro = ttl_bgn / EUR_TO_BGN
commission = ttl_euro * commission / 100
final_amount = ttl_euro - commission

print(f"{final_amount:.2f}")
