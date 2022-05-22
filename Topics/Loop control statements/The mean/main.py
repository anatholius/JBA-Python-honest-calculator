entry = None
numbers = list()
while entry != '.':
    entry = input()
    if entry != '.':
        numbers.append(int(entry))
print(sum(numbers) / len(numbers))
