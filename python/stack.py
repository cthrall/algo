import sys

from list import *

class Stack(LinkedList):
    def __init__(self):
        super(Stack, self).__init__()

    def push(self, value):
        temp = self.root
        self.root = Node(value)
        self.root.node = temp

    def pop(self):
        top = self.root
        self.delete(0)
        return top

def main(args):
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(stack.walk())

    stack.pop()
    print(stack.walk())

    stack.pop()
    print(stack.walk())

    stack.push(6)
    print(stack.walk())
    
    stack.pop()
    print(stack.walk())
    
if __name__ == '__main__':
    sys.exit(main(sys.argv))
