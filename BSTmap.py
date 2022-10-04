class NotFoundExeption(Exception):
    pass

class ItemExistsException(Exception):
    pass

class Node:
    def __init__(self, key, data = None, left = None, right = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        self.string = ''
        self._print_inorder(self.root)
        return self.string

    def _print_inorder(self, node):
        if node == None:
            return
        self._print_inorder(node.left)
        temp_str = f'{str(node.key)}: {str(node.data)}'
        self.string += '{' + temp_str + '} '
        self._print_inorder(node.right)

    def __len__(self):
        return self.size

    def __setitem__(self, key, data):
        pass

    def __getitem__(self, key):
        pass

    def insert(self, key, data):
        self.root = self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if node == None:
            return Node(key, data)
        if node.key < key:
            node.right = self._insert(node.right, key, data)
            return node
        elif node.key > key:
            node.left = self._insert(node.left, key, data)
            return node
        else:
            raise ItemExistsException()

    def update(self, key, data):
        pass

    def find(self, key):
        pass

    def contains(self, key):
        pass

    def remove(self, key):
        pass


tree = BSTMap()
tree.insert(5, 'a')
tree.insert(1, 'b')
tree.insert(8, 'c')
tree.insert(10, 'd')
tree.insert(2, 'e')
#tree.insert(2, 'e')
print(tree)