table = {}

using = True
while using:
    x = int(input("1. for add, 2. to search, 3. to exit: "))
    if x == 1:
        messages = input("Enter a message to get added to the table: ")
        table[hash(messages)] = messages
    elif x == 2:
        search = input("Enter the message you want to search for: ")
        search_hash = hash(search)
        if search_hash in table:
            print(f"Message found: {table[search_hash]}")
        else:
            print("Message not found.")
    elif x == 3:
        using = False
    else:
        print("Invalid option, please choose 1, 2, or 3.")
    
    print("\n \n")

    print(table)