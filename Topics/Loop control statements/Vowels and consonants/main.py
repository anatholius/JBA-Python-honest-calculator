entry = input()
vowels = 'aeiou'
for char in list(entry):
    if char.isalpha():
        print("vowel" if char in list(vowels) else 'consonant')
    else:
        break
