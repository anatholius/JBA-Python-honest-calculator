word = input()
underscore = '_'
for letter in word:
    if letter.isupper():
        word = word.replace(letter, underscore + letter.lower())
print(word)
