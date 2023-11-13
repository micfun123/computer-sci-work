age = input("How old are you? ")

if age:
    age = int(age)
    if age < 12:
        print("You are too young to drink")
    elif age >= 12 and age < 18:
        print("You can drink with a parent")
    else:
        print("You can drink")

#python match
def switch(age):
    rules = {
        1: "You are too young to drink",
        2: "You can drink with a parent",
        3: "You can drink"
    }
    match age:
        case 1 if age < 12:
            print(rules[1])
        case 2 if age >= 12 and age < 18:
            print(rules[2])
        case 3:
            print(rules[3])
        case _:
            print("Invalid age")


    