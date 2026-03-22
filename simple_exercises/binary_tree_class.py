
class Node:

    def __init__(self, value):
        self.value = value
        self.left_child: Node | None = None
        self.right_child: Node | None = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
    
    def add_node(self, entry):
        
        if self.root == None:
            self.root = Node(entry)

        else:
            self._insert_recursive(self.root, entry)
        
    def _insert_recursive(self, node: Node, entry):
        if node.value < entry:
            if node.right_child is None:
                node.right_child = Node(entry)
            else:
                self._insert_recursive(node.right_child, entry)
        if node.value > entry:
            if node.left_child is None:
                node.left_child = Node(entry)
            else:
                self._insert_recursive(node.left_child, entry)
         


        

    
