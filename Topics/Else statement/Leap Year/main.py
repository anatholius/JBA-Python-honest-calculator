year = int(input())

four_hundred = 400

print('Leap' if year % 4 == 0 and (year % 100 != 0 or year % four_hundred == 0) else 'Ordinary')
