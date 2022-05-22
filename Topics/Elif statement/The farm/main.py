animals = [
    'Chicken: 23',
    'Goat: 678',
    'Pig: 1296',
    'Cow: 3848',
    'Sheep: 6769',
]

money = input()
prices = list()
available = list()
POLY_S = 's'

for animal in animals:
    name = animal.split(': ')[0]
    price = float(animal.split(': ')[1])
    if price <= float(money):
        prices.append(price)
        available.append(name.lower())

if prices:
    most_expensive = max(prices)
    animal_name = available[prices.index(most_expensive)]
    count = round(float(money) // most_expensive)
    if count > 1 and animal_name != 'sheep':
        animal_name += POLY_S
    print(count, animal_name)
else:
    print('None')
