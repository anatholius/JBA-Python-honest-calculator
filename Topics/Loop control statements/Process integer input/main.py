process = True
while process:
    entry = int(input())
    if entry < 10:
        process = True
    elif entry > 100:
        process = False
    else:
        print(entry)
