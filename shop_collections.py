from collections import namedtuple

sales = namedtuple("customer", "ID_number First_name Sir_name Age Gender Product Price")
customers = []
currentID = 0

menu = """
Press 1 to add a sale\n
Press 2 to look up\n
press 3 to search for a customer\n"""
while True:
    x = int(input(menu))
    if x == 1:
        First_name = input("Enter First name: ")
        Sir_name = input("Enter Sir name: ")
        Age = input("Enter Age: ")
        Gender = input("Enter Gender: ")
        Product = input("Enter Product: ")
        Price = input("Enter Price: ")
        customers.append(
            sales(currentID, First_name, Sir_name, Age, Gender, Product, Price)
        )
        print(customers)
        currentID += 1
    elif x == 2:
        id = int(input("Enter ID number: "))
        for i in customers:
            if i.ID_number == id:
                print(i)

    elif x == 3:
        for i in customers:
            print(i)

    elif x == 4:
        exit()

    else:
        print("Invalid input")
