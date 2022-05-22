word = input()
upper_camel = ''.join(word.title().split())
print(upper_camel[0].lower() + upper_camel[1:])
