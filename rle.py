string = "cccaab"

def rle_encoder(string):
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

def rle_decoder(string):
    """
    rle(c3a2b1) -> cccaab
    """
    result = ""
    for i in range(0,len(string),2):
        result += string[i] * int(string[i+1])
    return result


print(rle_encoder(string))
print(rle_decoder(rle_encoder(string)))

