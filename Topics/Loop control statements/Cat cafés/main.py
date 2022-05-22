key = None
biggest = -1
name = ''
while key != 'MEOW':
    check = input().split(' ')
    key = check[0]
    if len(check) == 2 and int(check[1]) > biggest:
        biggest = int(check[1])
        name = check[0]
print(name)
