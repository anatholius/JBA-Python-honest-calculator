string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
# 1. First solution
# count = 0
# for letter in list(string):
#     if letter in vowels:
#         count += 1
# print(count)

# 2. Smart and beautiful solution
print(sum(letter in vowels for letter in string))
