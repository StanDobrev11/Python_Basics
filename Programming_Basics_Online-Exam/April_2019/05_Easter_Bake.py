from math import ceil

# weight in grams
FLOUR_PCKT = 750
SUGAR_PCKT = 950

sugar_grams_req = 0
flour_grams_req = 0
sugar_max = 0
flour_max = 0

easter_bread = int(input())
for bread in range(easter_bread):
    sugar_needed = int(input())
    flour_needed = int(input())
    sugar_grams_req = sugar_grams_req + sugar_needed
    flour_grams_req = flour_grams_req + flour_needed
    if sugar_needed > sugar_max:
        sugar_max = sugar_needed
    if flour_needed > flour_max:
        flour_max = flour_needed

flour_pckt_req = ceil(flour_grams_req / FLOUR_PCKT)
sugar_pckt_req = ceil(sugar_grams_req / SUGAR_PCKT)

print(
    f"Sugar: {sugar_pckt_req}\nFlour: {flour_pckt_req}\nMax used flour is "
    f"{flour_max} grams, max used sugar is {sugar_max} grams.")