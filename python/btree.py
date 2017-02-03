import sys

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if node.value == value:
            return
        else:
            if value < node.value:
                if node.left == None:
                    node.left = Node(value)
                else:
                    self._insert(node.left, value)
            else:
                if node.right == None:
                    node.right = Node(value)
                else:
                    self._insert(node.right, value)
        
    def __getitem__(self, value):
        return self._getitem(self.root, value)

    def _getitem(self, node, value):
        if node == None or node.value == value:
            return node
        else:
            if value < node.value:
                return self._getitem(node.left, value)
            else:
                return self._getitem(node.right, value)
        
    def depth(self):
        return self._depth(self.root, 1)

    def _depth(self, node, d):
        if node.left != None:
            return self._depth(node.left, d+1)

        if node.right != None:
            return self._depth(node.right, d+1)

        if node.left == None and node.right == None:
            return d
            
    def walk(self):
        depth = self.depth()
        output = [[] for i in range(depth)]
        return self._walk(output, self.root, 0)

    def _walk(self, output, node, level):
        output[level].append(node.value)

        if node.left != None:
            self._walk(output, node.left, level + 1)

        if node.right != None:
            self._walk(output, node.right, level + 1)

        return output

def main(args):
    tree = BinaryTree()
    inputs = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
    for i in inputs:
        tree.insert(i)

    print(tree.depth())
    print(tree.walk())

    node = tree[4]
    print(node)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
