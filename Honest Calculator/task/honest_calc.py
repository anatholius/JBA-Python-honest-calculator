msg_ = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)",
]

memory = float(0)

delimiter = None
x, y, op = None, None, None


def is_number(n):
    return str(n).replace('.', '').isnumeric()


def is_one_digit(d):
    return True if float(d).is_integer() and -10 < d < 10 else False


def check(a, b, c):
    msg = ""

    if is_one_digit(a) and is_one_digit(b):
        msg += msg_[6]

    if (a == 1 or b == 1) and c == "*":
        msg += msg_[7]

    if (a == 0 or b == 0) and c in list("*+-"):
        msg += msg_[8]

    if msg != '':
        msg = msg_[9] + msg
        print(msg)


while delimiter != '.':
    print(msg_[0])

    # read calc  and  split into variables
    try:
        x, op, y = input().split()
    except ValueError:
        print('You must provide `x op y` separated by spaces! Try again...')
        continue

    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    # check if x, y are numbers
    if not is_number(x) or not is_number(y):
        print(msg_[1])
        continue

    x = float(x)
    y = float(y)

    # check if op is allowed operation
    if op in '+-*/':
        check(x, y, op)
    else:
        print(msg_[2])
        continue

    # calculate:
    global result
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        if y == 0:
            print(msg_[3])
            continue
        result = x / y

    print(result)

    # continue calculating or not?
    storing_answer = None
    while storing_answer != 'n':
        print(msg_[4])
        storing_answer = input()
        if storing_answer == 'y':
            one_digit = is_one_digit(result)
            if one_digit:
                msg_index = 10

                confirm_answer = None
                while confirm_answer != 'n':
                    print(msg_[msg_index])
                    confirm_answer = input()
                    if msg_index < 12:
                        msg_index += 1
                    else:
                        memory = result
                        confirm_answer = 'n'
            else:
                memory = result

            break

    print(msg_[5])
    if input() == 'n':
        break

# print('Thanks for calculating!')
