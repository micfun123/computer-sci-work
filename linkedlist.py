
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def delete(self, data):
        temp = self.head
        if temp.data == data:
            self.head = temp.next
            return
        while temp.next != None:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev



if __name__ == "__main__":
    llist = LinkedList()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)
    llist.insert(6)
    llist.insert(7)
    llist.printList()
    llist.delete(3)
    llist.printList()
    llist.reverse()
    llist.printList()

    