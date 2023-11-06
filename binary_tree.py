
class BinaryTree:
    def __init__(self,value) -> None:
        self.left = None
        self.right = None
        self.value = value

    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)
        else:
            self.value = value

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

    def find(self,value):
        if value < self.value:
            if self.left is None:
                return str(value)+" Not Found"
            return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return str(value)+" Not Found"
            return self.right.find(value)
        else:
            return str(self.value)+" Found"
        

tree = BinaryTree(12)
tree.insert(6)
tree.insert(14)
tree.insert(3)
tree.print_tree()
print(tree.find(7))
print(tree.find(14))
