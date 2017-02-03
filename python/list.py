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

    def __getitem__(self, index):
        return self._getitem(self.root, index, 0)

    def _getitem(self, node, index, i):
        if index == i:
            return node.value
        else:
            if node == None:
                raise IndexError
            else:
                return self._getitem(node.node, index, i + 1)

    def delete(self, index):
        if index == 0:
            self.root = self.root.node
        else:
            return self._delete(self.root, index, 0, None)

    def _delete(self, node, index, i, prev):
        if index == i:
            prev.node = node.node
        else:
            self._delete(node.node, index, i + 1, node)
    
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
    
    print(list[0])
    print(list[1])

    list.delete(0)
    print(list.walk())

    list.delete(1)
    print(list.walk())

if __name__ == '__main__':
    sys.exit(main(sys.argv))
