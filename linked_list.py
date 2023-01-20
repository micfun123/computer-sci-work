
linked_list_example = [["a",2],["d",3],["c",1],["e",None]]

def print_linked_list(linked_list_example):
    #link list in the format [data, next]
    possition = 0
    while linked_list_example[possition][1] != None:
        print(linked_list_example[possition][0],linked_list_example[possition][1])
        possition = linked_list_example[possition][1]
    print(linked_list_example[possition][0],linked_list_example[possition][1])

def add_item(linked_list_example, new_item):
    #link list in the format [data, next]
    possition = 0
    while linked_list_example[possition][1] != None:
        possition = linked_list_example[possition][1]
    linked_list_example.append([new_item, None])
    linked_list_example[possition][1] = len(linked_list_example)-1
    #sort the pointers
    for i in range(0,len(linked_list_example)-1):
        if linked_list_example[i][0] > linked_list_example[i+1][0]:
            linked_list_example[i][1] = i+1
            linked_list_example[i+1][1] = i
    print_linked_list(linked_list_example)
    print("\n\n")

while True:
    print("Press 1 to view the linked list")
    print("Press 2 to add a new item to the linked list")
    print("Press 3 to remove an item from the linked list")
    print("Press 4 to exit")
    choice = int(input("What would you like to do? "))
    if choice == 1:
        print_linked_list(linked_list_example)
        print("\n\n")
    elif choice == 2:
        new_item = input("What would you like to add? ")
        add_item(linked_list_example, new_item)
        
