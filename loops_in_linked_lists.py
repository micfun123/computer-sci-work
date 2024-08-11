class LinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def print_list(self):
        node = self
        while node:
            print(node.data, end=' -> ')
            node = node.next
        print('None')

    def loop_check(self):
        node = self
        slow = node.next
        fast = node.next.next
        while (fast != None):
            if slow == fast:
                return True
            else:
                fast = fast.next.next
                slow = slow.next
        return False


head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)

print(head.loop_check())

