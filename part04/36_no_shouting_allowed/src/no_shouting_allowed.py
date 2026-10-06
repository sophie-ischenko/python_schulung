def no_shouting(strings):
    result = []

    for string in strings:
        if not string.isupper():
            result.append(string)

    return result


my_list = [
    "ABC",
    "def",
    "UPPER",
    "ANOTHERUPPER",
    "lower",
    "another lower",
    "Capitalized"
]

pruned_list = no_shouting(my_list)

print(pruned_list)