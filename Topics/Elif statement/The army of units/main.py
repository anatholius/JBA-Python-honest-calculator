elephants = [10, 50, 500, 1000]
frogs = ['no army', 'few', 'pack', 'horde', 'swarm', 'legion']

snake = int(input())

if snake == 0:
    print(frogs[0])
else:
    prev = 1
    for period in elephants:
        if prev <= snake < period:
            print(frogs[elephants.index(period) + 1])
            prev = period
            break
    else:
        print(frogs[5])
