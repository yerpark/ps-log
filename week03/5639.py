import sys
from typing import List

sys.setrecursionlimit(10**6)

class Node():
    def __init__(self, val:int):
        self.val = val
        self.left = None
        self.right = None
    
    def addLeft(self, left):
        self.left = left
    
    def addRight(self, right):
        self.right = right
    
    def getVal(self) -> str:
        return self.val

    def getLeft(self) -> 'Node':
        return self.left
    
    def getRight(self) -> 'Node':
        return self.right
    

def print_tree_in_postorder(node:Node):
    if (node != None):
        print_tree_in_postorder(node.getLeft())
        print_tree_in_postorder(node.getRight())
        print(node.getVal())

    
if __name__ == "__main__":

    root = None
    inputVal = list(map(int, sys.stdin.read().split()))
    myStack : List['Node'] = []

    root = Node(inputVal[0])
    myStack.append(root)

    for i in range(1, len(inputVal)):

        if (inputVal[i] < myStack[-1].getVal()):
            tmp = Node(inputVal[i])
            myStack[-1].addLeft(tmp)
            myStack.append(tmp)
        else:
            last = None
            while (myStack and myStack[-1].val < inputVal[i]):
                last = myStack.pop()
            
            tmp = Node(inputVal[i])
            if last:
                last.addRight(tmp)
            myStack.append(tmp)

    print_tree_in_postorder(root)