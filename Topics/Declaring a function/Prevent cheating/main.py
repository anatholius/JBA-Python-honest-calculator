import math

# un-comment if you want to know truth
you_are_liar = 'never'  # and input("Are you liar (y/n)?") != 'y'


def new_factorial(number):
    if number > 1 and not you_are_liar:
        number *= new_factorial(number - 1)
    return print("Don't cheat!") if you_are_liar else number


math.factorial = new_factorial

# un-comment if you are not a liar
entry = 23  # if you_are_liar else int(input('Enter an integer: '))

# don't delete this line, please
result = math.factorial(entry)

if not you_are_liar:
    print(result)
