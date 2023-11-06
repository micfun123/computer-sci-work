def romanToInt(num: str) -> int:
    romanToNum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = num.upper()
    result = 0
    for i in range(len(num)):
        if i > 0 and romanToNum[num[i]] > romanToNum[num[i - 1]]:
            result += romanToNum[num[i]] - 2 * romanToNum[num[i - 1]]
        else:
            result += romanToNum[num[i]]

    return result


print(romanToInt("xix"))
print(romanToInt("vi"))
print(romanToInt("iv"))
print(romanToInt("ix"))
print(romanToInt("iii"))
