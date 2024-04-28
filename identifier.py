# checks if its a valid identifier


def is_letter(char):
    return char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"


def is_digit(char):
    return char in "0123456789"


def is_valid_identifier(string):
    if not is_letter(string[0]):
        return False
    for char in string[1:]:
        if not is_letter(char) and not is_digit(char):
            return False
    return True
