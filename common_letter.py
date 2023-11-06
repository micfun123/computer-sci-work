teststr = "eaeeeeeedawdawdawd"


def common_letter(teststr):
    teststr = teststr.lower()

    letters = {}  # makes a dictionary of letters and their counts

    for letter in teststr:
        if letter in letters:
            letters[letter] += 1  # adds to count if letter already in dictionary
        else:
            letters[letter] = 1  # adds letter to dictionary if not already there

    maxletter = ""  # placeholder for most common letter name
    maxcount = 0  # placeholder for most common letter count
    for letter in letters:
        if (
            letters[letter] > maxcount
        ):  # checks if current letter is more common than previous most common letter
            maxletter = letter
            maxcount = letters[letter]  # sets new most common letter and count
    return maxletter


print(common_letter(teststr))
