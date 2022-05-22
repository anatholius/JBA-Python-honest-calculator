entry = None
entries = list()
while not entry or sum(entries) != 0:
    entry = input()
    entries.append(int(entry))
print(sum(n ** 2 for n in entries))
