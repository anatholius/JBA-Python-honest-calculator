x = float(input())
y = float(input())

if x == 0 and y == 0:
    print("It's the origin!")
elif x == 0 or y == 0:
    print("One of the coordinates is equal to zero!")

if x > 0 and y > 0:
    print('I')
elif y < 0 < x:
    print('IV')
elif x < 0 < y:
    print('II')
elif x < 0 and y < 0:
    print('III')
