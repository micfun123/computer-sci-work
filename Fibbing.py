a = 0
b = int(input("enter the starting value: "))
amount = int(input("How many places should it go up to: "))
z = 0

total = 0
list = []

for i in range(amount):
    z = a + b
    total = total + z
    list.append(z)
    a = b
    b = z

print(list)
print(f"The total amount of all the numbers is: {total}")
print(f"Your array backwards is {list[::-1]}")

