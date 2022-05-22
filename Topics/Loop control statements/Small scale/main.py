entry = None
floats = list()
while entry != '.':
    entry = input()
    if entry != '.':
        floats.append(float(entry))
print(min(floats))
