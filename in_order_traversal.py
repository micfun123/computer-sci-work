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


root = Node("Banana")
root.left = Node("apple")
root.right = Node("Dog")
root.left.left = Node("aaaaa")
root.left.right = Node("Van")
# Function call
print("\nInorder traversal of binary tree is")
printInorder(root)

nodes = []
while True:
    print("1. Add a node")
    print("2. Print the tree")
    print("4. Exit")
    choice = input("Enter your choice: ")