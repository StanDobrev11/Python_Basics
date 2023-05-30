import math

n = int(input())

if n <= 0:
    print("Not prime")

is_prime = True
for x in range(2, n):
    if n % x == 0:  # not prime
        is_prime = False

if is_prime:
    print("Prime")
else:
    print("Not Prime")

# for x in range(1, round(math.sqrt(n)) + 1):
#     if n % x == 0:
#         print("Not prime")
#         break
#     else:
#         print("Prime")
#         break

# is_prime = True
# for x in range(1, n + 1):
#     if n % x == 0:
#         is_prime = False
#         break
# if is_prime:
#     print("Prime")
# else:
#     print("Not prime")
