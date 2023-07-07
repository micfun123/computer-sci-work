string = "cccaab"

def rle(string):
    """
    rle(cccaab) -> c3a2b1
    """
    result = ""
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            result += string[i] + str(count)
            count = 1
    result += string[i] + str(count)
    return result

print(rle(string))
