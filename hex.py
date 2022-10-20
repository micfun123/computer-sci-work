raw_num = int(input("Enter a number: "))

def tohex(num):
    hex = []
    while num > 0:
        if num % 16 > 9:
            hex.append(chr(num % 16 + 55))
        else:
            hex.append(num % 16)
        num = num // 16
    hex = hex[::-1]
    return hex

print(tohex(raw_num))
