import random
num = []
for i in range(1000):
    add = random.randint(100,999)
    num.append(add)

num.sort()
strnum = [str(i) for i in num]
print(strnum)

#would u want to print the list in a file?
with open('num.txt','w') as f:
    for i in strnum:
        f.write(f"'{i}', ")
