class Node(object):

    def __init__(self, data):
        self.r_child = None
        self.l_child = None
        self.data = data


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_node(self.root, data)

    def _insert_node(self, current_node, data):
        if current_node.data > data:
            if current_node.l_child is None:
                current_node.l_child = Node(data)
            else:
                self._insert_node(current_node.l_child, data)
        else:
            if current_node.r_child is None:
                current_node.r_child = Node(data)
            else:
                self._insert_node(current_node.r_child, data)

    def get_root(self):
        return self.root

    def print_in_order(self, node):
        if not node:
            return

        print(node.data)
        if node.l_child is not None:
            self.print_in_order(node.l_child)
        if node.r_child is not None:
            self.print_in_order(node.r_child)

    def delete(self, key):
        pass

    def search(self, key):
        pass


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(8)
    bst.insert(12)
    bst.insert(1)
    bst.insert(0)
    bst.insert(20)
    bst.print_in_order(bst.get_root())
    #print(bst.search(1))
    #bst.delete(10)
    #print(bst.search(10))
