string = "cccaab"


def rle_encoder(string):
    """
    rle(cccaab) -> c3a2b1
    """
    result = ""
    count = 1
    for i in range(0, len(string)):
        if i == 0:
            result += string[i]
        elif string[i] == string[i - 1]:
            count += 1
        else:
            result += str(count) + string[i]
            count = 1
    result += str(count)
    return result


print(rle_encoder(string))
