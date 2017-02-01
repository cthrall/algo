import sys

class Node(object):
    def __init__(self, value):
        self.value = value
        self.node = None

class LinkedList(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if node.node == None:
            node.node = Node(value)
        else:
            self._insert(node.node, value)

    def __len__(self):
        if self.root == None:
            return 0
        else:
            return self._len(self.root, 1)

    def _len(self, node, d):
        if node.node == None:
            return d
        else:
            return self._len(node.node, d+1)

    def walk(self):
        output = []
        return self._walk(output, self.root)

    def _walk(self, output, node):
        output.append(node.value)
        
        if node.node == None:
            return output
        else:
            return self._walk(output, node.node)

def main(args):
    list = LinkedList()
    inputs = [1, 2, 3, 4, 5]
    for i in inputs:
        list.insert(i)

    print(len(list))
    print(list.walk())

if __name__ == '__main__':
    sys.exit(main(sys.argv))
