num = 1
valid = False
while num <= 15:
    while not valid:
            inputed = int(input("Enter a number between 1 and 3: "))
            if num < 1 or num > 3:
                print("Invalid number")
            else:
                valid = True
                num = num + inputed
                print(num)
    if num == 15:
        print("player one does not win")
        break
    valid = False
    while not valid:
            inputed = int(input("Enter a number between 1 and 3: "))
            if num < 1 or num > 3:
                print("Invalid number")
            else:
                valid = True
                num = num + inputed
                print(num)
    if num == 15:
        print("player two does not win")
        break
    valid = False
