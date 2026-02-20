from typing import List
import sys

class myNode():
    def __init__(self, value:str):
        self.value = value
        self.left = None
        self.right = None
    
    def addLeft(self, left):
        self.left = left
    
    def addRight(self, right):
        self.right = right
    
    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right
    
    def getValue(self):
        return self.value


def preorder_recursive(node:myNode):

    if (node != None):
        print(node.getValue(), end="")
        preorder_recursive(node.getLeft())
        preorder_recursive(node.getRight())

def inorder_recursive(node:myNode):

    if (node != None):
        inorder_recursive(node.getLeft())
        print(node.getValue(), end="")
        inorder_recursive(node.getRight())

def postorder_recursive(node:myNode):

    if (node != None):
        postorder_recursive(node.getLeft())
        postorder_recursive(node.getRight())
        print(node.getValue(), end="")

def findNode(parent:myNode, val:str) -> myNode :
    
    if (parent != None):
        if (parent.getValue() == val):
            return parent
        left = findNode(parent.getLeft(), val)
        if (left != None):
            return left
        right = findNode(parent.getRight(), val)
        if (right != None):
            return right
        return None
    else:
        return None



if __name__ == "__main__":
    
    n = int(sys.stdin.readline().strip())

    root = None

    for _ in range(n):
        inputVal = sys.stdin.readline().split()

        if (root == None):
            root = myNode(inputVal[0])
            parent = root
        else:
            parent = findNode(root, inputVal[0])

        if (inputVal[1] != '.'):
            parent.addLeft(myNode(inputVal[1]))
        if (inputVal[2] != '.'):
            parent.addRight(myNode(inputVal[2]))
        


    preorder_recursive(root)
    print("")
    inorder_recursive(root)
    print("")
    postorder_recursive(root)
    print("")
