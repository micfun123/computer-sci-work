
queue = ["cat", "dog", "bird", "fish","cow"]


def enqueue(thing,queue):
    queue.append(thing)
    print(queue)

def dequeue(queue):
    item = queue.pop(0)
    return item

def peek(queue):
    print(f"the first item in the queue is {queue[0]}")
    print(f"the last item in the queue is {queue[-1]}")
    print(f"Heres the whole queue: {queue}")


while True:
    print("""
    press 1 to add to queue
    press 2 to remove from queue
    press 3 to peek at queue
    press 4 to quit
    """)

    option = int(input("Enter your choice: "))
    if option == 1:
        add = input("Enter what you would like to add: ")
        enqueue(add,queue)
    if option == 2:
        thing = dequeue(queue)
        print(thing)
    if option ==3:
        peek(queue)
    if option ==4:
        break
        
