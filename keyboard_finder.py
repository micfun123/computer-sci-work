configuration_of_keyboard = [
    ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
    ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";"],
    ["z", "x", "c", "v", "b", "n", "m", ",", ".", "/"],
]


def find_quards(key):
    for i in range(len(configuration_of_keyboard)):
        for j in range(len(configuration_of_keyboard[i])):
            if configuration_of_keyboard[i][j] == key:
                return i, j


print(find_quards("c"))
