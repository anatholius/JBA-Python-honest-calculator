entry = input().split()
print(round(len([note for note in entry if note == 'A']) / len(entry), 2))
