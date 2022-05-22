numbers = list()
got = None
forbidden = 55
while got != forbidden:
    got = int(input())
    if got != forbidden:
        numbers.append(got)
print(len(numbers))
print(sum(numbers))
print(round(sum(numbers) / len(numbers)))
