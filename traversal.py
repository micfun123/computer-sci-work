class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#store all nodes in a form of list
nodes = {}


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


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def binnary_tree_show(root):
    print(root.val)
    if root.left is not None:
        binnary_tree_show(root.left)
    if root.right is not None:
        binnary_tree_show(root.right)




while True:
    print("1. Add a node")
    print("2. Print the tree")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        node = Node(input("Enter a root node: "))
        if node.val in nodes:
            print("Node already exists")
        else:
            nodes[node.val] = node
            if len(nodes) == 1:
                root = node
            else:
                insert(root, node)
    elif choice == "2":
        print("\n Inorder traversal of binary tree is\n ")
        printInorder(root)
        print("\n Postorder traversal of binary tree is\n ")
        printPostorder(root)
        print("\n Preorder traversal of binary tree is\n ")
        printPreorder(root)

    elif choice == "3":
        break
    elif choice == "4":
        for i in nodes:
            print(i)
    elif choice == "5":
        binnary_tree_show(root)
        
    else:
        print("Invalid choice")
                
