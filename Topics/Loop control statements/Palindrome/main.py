word = input()
# 1. with list reversion
# print('Palindrome' if list(word) == list(reversed(word)) else 'Not palindrome')
# 2. with string reversion
print('Palindrome' if word == word[::-1] else 'Not palindrome')
