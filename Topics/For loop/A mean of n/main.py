count = int(input())
numbers = list()
for _ in range(count):
    numbers.append(int(input()))
print(sum(numbers) / len(numbers))
