
linked_list_example = [["a",2],["d",3],["c",1],["e",None]]

def print_linked_list(linked_list_example):
    #link list in the format [data, next]
    possition = 0
    while linked_list_example[possition][1] != None:
        print(linked_list_example[possition][0])
        possition = linked_list_example[possition][1]
    print(linked_list_example[possition][0])




while True:
    print("Press 1 to view the linked list")
    print("Press 2 to add a new item to the linked list")
    print("Press 3 to remove an item from the linked list")
    print("Press 4 to exit")
    choice = int(input("What would you like to do? "))
    if choice == 1:
        print_linked_list(linked_list_example)
    elif choice == 2:
        
