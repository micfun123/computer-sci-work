def timestable():
    x = int(input(" Please enter the times table you want to know: "))
    for i in range(12):
        print(f"{x} * {i} = {x*i}")
    print()
    main()


def vat():
    x = float(input(" Please enter price so vat can be added: "))
    x = x + x * 0.2
    print(f" Your price with vat is now {x}")
    print()
    main()


def taxs():
    x = float(input("Enter your salary"))
    if x < 12570:
        print("your total tax amount if $0")
    elif x >= 12571 and x < 50270:
        print(f"your tax amount on {x} is {x * 0.2}")
    elif x >= 50271 and x < 150000:
        print(f"your tax amount on {x} is {x * 0.4}")
    elif x >= 150000:
        print(f"your tax amount on {x} is {x * 0.45}")
        print()
    main()


def main():
    print(
        """
    press 1 for times tables
    press 2 for vat calc
    press 3 for taxs calc
    """
    )
    option = int(input())
    if option == 1:
        timestable()
    elif option == 2:
        vat()
    elif option == 2:
        taxs()
    else:
        print("please enter a valid input")
        main()


main()
