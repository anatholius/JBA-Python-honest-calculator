string = input()

replacements = ',.!?'

result = string
for symbol in replacements:
    result = result.replace(symbol, '')
print(result.lower())
