from collections import namedtuple

sales = []
currentid = 0

sale = namedtuple("sale", "ID First_name Surname age Gender Product Price")

def newsale():
    global currentid
    global sales
    firstname = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    age = int(input("Enter your age: "))
    gender = input("enter your gender: ")
    product = input("enter your product: ")
    price = float(input("enter your price: "))
    #add to list
    currentid += 1
    sales.append(
        sale(
            currentid, firstname,surname,age,gender,product,price
    ))

def view():
    for i in sales:
        print(i)

#menu
while True:
    print("1. New sale")
    print("2. View sales")
    print("3. Exit")
    option = input("Enter your option: ")
    if option == "1":
        newsale()
    elif option == "2":
        view()
    elif option == "3":
        break
    else:
        print("Invalid option")