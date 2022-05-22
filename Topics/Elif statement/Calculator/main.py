first_number = float(input())
second_number = float(input())
operator = input()

result = None

if operator in ['/', 'mod', 'div'] and second_number == 0:
    print("Division by 0!")
else:
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    if operator == 'pow':
        result = first_number ** second_number
    elif operator == '/':
        result = first_number / second_number
    elif operator == 'mod':
        result = first_number % second_number
    if operator == 'div':
        result = first_number // second_number
    print(result)
