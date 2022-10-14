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
    

stuff = [128, 68 , 32 , 16 , 8 , 4 , ]
x = int(input("Enter da number: "))
while x < 0 or x > 255:
    print("invalid")
    x = int(input("Enter da number: "))


tobin(x)
realnum = realnum[::-1]
print(realnum)
    





    

