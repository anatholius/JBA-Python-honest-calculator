a = int(input())
b = 0
while a > b:
    b = int(input())
    if a > b:
        print("B should be grater then A")
h = int(input())

if h < a:
    print("Deficiency")
elif h > b:
    print("Excess")
else:
    print("Normal")
