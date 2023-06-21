
teststr = "eadawdawdawd"

def common_letter(teststr):
    teststr = teststr.lower()
    letters = {}
    for letter in teststr:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    print(letters)


print(common_letter(teststr))
