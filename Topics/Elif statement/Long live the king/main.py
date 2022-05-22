x = int(input())
y = int(input())

# first solution
if x == 1:
    if y in [1, 8]:
        moves_1 = 3
    else:
        moves_1 = 5
elif x == 8:
    if y in [1, 8]:
        moves_1 = 3
    else:
        moves_1 = 5
else:
    if y in [1, 8]:
        moves_1 = 5
    else:
        moves_1 = 8

# better solution
if x in (1, 8) and y in (1, 8):
    moves_2 = 3
elif x in (1, 8) and y not in (1, 8) or x not in (1, 8) and y in (1, 8):
    moves_2 = 5
else:
    moves_2 = 8

moves = moves_2
print(moves)
