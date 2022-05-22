given = int(input())
time = 10.5
target = time + given
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday']
day = days[1]
if target < 0:
    day = days[0]
elif target > 24:
    day = days[2]

print(day)
