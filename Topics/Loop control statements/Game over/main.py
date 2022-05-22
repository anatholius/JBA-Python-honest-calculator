scores = input().split()
# put your python code here
errors = 0
corrects = 0
for score in scores:
    error = score == 'I'
    errors += 1 if error else 0
    if errors == 3:
        print('Game over')
        print(corrects)
        break
    if not error:
        corrects += 1
else:
    print('You won')
    print(corrects)
