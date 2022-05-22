number = int(input())
word = input()

# write a condition for plurals
pluralize = ""
if number != 1:
    pluralize = "s"

print(number, word + pluralize)
