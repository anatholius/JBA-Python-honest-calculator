number = int(input())
result = number
while number > 1:
    number -= 1
    result *= number
print(result)
