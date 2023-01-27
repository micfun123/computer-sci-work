#python stack files

stack = []

def add(data):
    stack.append(data)

def pop():
    data = stack[-1]
    del stack[-1]
    return data

def peek():
    return stack[-1]

def show():
    print(stack)

for index in range(10):
    add(index)
 
while True:
    print("""\n 
    1. to add to the stack\n
    2. to pop from the stack\n
    3. to peek at the stack\n
    4. to print the stack\n
    5. to exit\n""")	

    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to add: "))
        add(data)
    elif choice == 2:
        data = pop()
        print("Popped data is: ", data)
    elif choice == 3:
        print("Data at the top is: ", peek())
    elif choice == 4:
        show()
    elif choice == 5:
        exit()

