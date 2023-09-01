male_clients = int(input())
female_clients = int(input())
tables = int(input())

tables_count = 0
for male_client in range(1, male_clients + 1):
    for female_client in range(1, female_clients + 1):
        if tables_count >= tables:
            break
        print(f"({male_client} <-> {female_client})", end=" ")
        tables_count += 1
