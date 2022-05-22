deposit = int(input())
LIMIT = 700000
years = 0
progress = 1.071
while deposit < LIMIT:
    deposit *= progress
    years += 1
print(years)
