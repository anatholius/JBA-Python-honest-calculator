first = int(input())
second = int(input())

total = 0
count = 0

for number in range(first, second + 1):
    if number % 3 == 0:
        total += number
        count += 1

average = total / count
print(average)
