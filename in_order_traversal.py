class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):

    if root:

        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)

def printPostorder(root):

    if root:

        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),

def printPreorder(root):
    
        if root:
    
            # First print the data of node
            print(root.val),
    
            # Then recur on left child
            printPreorder(root.left)
    
            # Finally recur on right child
            printPreorder(root.right)


root = Node("Banana")
root.left = Node("apple")
root.right = Node("Dog")
root.left.left = Node("aaaaa")
root.left.right = Node("Van")
# Function call
print("\nInorder traversal of binary tree is")
printInorder(root)
print("\nPostorder traversal of binary tree is")
printPostorder(root)
print("\nPreorder traversal of binary tree is")
printPreorder(root)

