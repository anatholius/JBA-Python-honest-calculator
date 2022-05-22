age = int(input())

young = 17
middle = 26
mature = 41
old = 61

if age < young:
    print("Lion King")
if age >= old:
    print("Breakfast at Tiffany's")

if young <= age < middle:
    print("Trainspotting")
elif middle <= age < mature:
    print("Matrix")
elif mature <= age < old:
    print("Pulp Fiction")
