def ispaladrome(x :int) -> bool:
    return str(x) == str(x)[::-1]

print(ispaladrome(12321))