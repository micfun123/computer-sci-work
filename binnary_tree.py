tree = {}

def add_node(node, parent=None):
    if parent is None:
        tree[node] = None
    else:
        tree[node] = parent
    item = input("Enter a child node (or nothing to stop): ")
    if item != "":
        add_node(item, node)



def print_tree(node, level=0):
    print(" " * level + node)
    for k, v in tree.items():
        if v == node:
            print_tree(k, level + 1)


exited = False
while not exited:
    print("1. Add a node")
    print("2. Print the tree")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_node(input("Enter a root node: "))
    elif choice == "2":
        print_tree(input("Enter the root node: "))
    elif choice == "3":
        print(tree)
    elif choice == "4":
        exited = True
    else:
        print("Invalid choice")