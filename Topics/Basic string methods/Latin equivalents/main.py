name = input()


def normalize(new_name):
    replacements = [
        ["ë", "e"],
        ["é", "e"],
        ["á", "a"],
        ["å", "a"],
        ["œ", "oe"],
        ["æ", "ae"],
    ]
    for symbol in replacements:
        new_name = new_name.replace(symbol[0], symbol[1])

    return new_name


print(normalize(name))
