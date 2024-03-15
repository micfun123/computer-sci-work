
#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


num1 = ListNode(2, ListNode(4, ListNode(3)))
num2 = ListNode(5, ListNode(6, ListNode(4)))


def addTwoNumbers(l1, l2):
    #turned the linked list in to a regular list

    arr1 = []
    arr2 = []
    while l1:
        arr1.append(l1.val)
        l1 = l1.next
    while l2:
        arr2.append(l2.val)
        l2 = l2.next
    
    #reversed the list
    arr1 = arr1[::-1]
    arr2 = arr2[::-1]

    n1 = int(''.join(map(str, arr1)))
    n2 = int(''.join(map(str, arr2)))
    
    #flip it back to a linked list
    n3 = str(n1+n2)[::-1]
    l3 = ListNode(int(n3[0]))
    current = l3
    for i in range(1, len(n3)):
        current.next = ListNode(int(n3[i]))
        current = current.next
    return l3

print(addTwoNumbers(num1,num2))