realnum = []
negnumb = []


def tobin(num):
    for i in range(8):
        if num % 2 == 0:
            realnum.append(0)
            num = num / 2
        else:
            realnum.append(1)
            num = (num - 1) / 2
    
def two_complement(hand_the_bin_over):
    for i in realnum:
        if i == 1:
            negnumb.append(0)
        else:
            negnumb.append(1)
    addone()

def addone():
    global negnumb
    negnumb = negnumb[::-1]
    carry = 0
    if negnumb[0] == 0:
        negnumb[0] = 1
    else:
        for i in range(8):
            if negnumb[i] == 0:
                negnumb[i] = 1
                carry = 0
                break
            else:
                negnumb[i] = 0
                carry = 1


    negnumb = negnumb[::-1]

x = int(input("Enter da number: "))
while x < 0 or x > 255:
    print("invalid")
    x = int(input("Enter da number: "))


tobin(x)
realnum = realnum[::-1]
print(f"Your number in binary is {realnum}")
two_complement(realnum)

print(f"Your neg number in binary is {negnumb}")


    
