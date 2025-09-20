# 노드 구현
# 트리 구현

# 입력 -> 전위 순회 결과 -> 노트 계속 왼쪽에 추가하다가 값이 전 값보다 커지는 순간 오른쪽 추가 

import sys

class Node():
    def __init__(self, val:int):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
    
    def addLeft(self, left):
        self.left = left
    
    def addRight(self, right):
        self.right = right

    def addParent(self, parent):
        self.parent = parent
    
    def getVal(self) -> str:
        return self.val

    def getLeft(self) -> 'Node':
        return self.left
    
    def getRight(self) -> 'Node':
        return self.right
    
    def getParent(self) -> 'Node':
        return self.parent
    
def print_tree_in_preorder(node:Node):
    if (node != None):
        print(node.getVal())
        print_tree_in_preorder(node.getLeft())
        print_tree_in_preorder(node.getRight())

def print_tree_in_postorder(node:Node):
    if (node != None):
        print_tree_in_postorder(node.getLeft())
        print(node.getVal())
        print_tree_in_postorder(node.getRight())

if __name__ == "__main__":
    inputVal = list(map(int, sys.stdin.read().split()))
    root = None
    lastNode = None

    for i in range(len(inputVal)):
        if (root == None):
            root = Node(inputVal[i])
            lastNode = root
            continue

        if (inputVal[i] < lastNode.getVal()):
            tmp = Node(inputVal[i])
            lastNode.addLeft(tmp)
            tmp.addParent(lastNode)
            lastNode = tmp

        else: #같은 케이스는 없음 #parent의 값이랑도 비교해야 
            noMoreWorkFlag = False
            while (noMoreWorkFlag != True):
                parent = lastNode.getParent()
                if (parent == None):
                    tmp = Node(inputVal[i])
                    lastNode.addRight(tmp)
                    tmp.addParent(lastNode)
                    lastNode = tmp
                    noMoreWorkFlag = True 
                elif (inputVal[i] < parent.getVal()) :
                    tmp = Node(inputVal[i])
                    lastNode.addRight(tmp)
                    tmp.addParent(lastNode)
                    lastNode = tmp
                    noMoreWorkFlag = True
                else :
                    lastNode = lastNode.parent

    print("------------------------DEBUG")
    print_tree_in_postorder(root)


#위코드의 문제점: 언젠가 값이 큰 부모가 나타날 것이라고 가정
#중요한 것 : 한 방향으로만 가기 때문에 (/)
#오른쪽 노드들까지 가지 못함

# 그것보다는 전위순위로 값을 입력받기 때문에 자기 보다 앞에 있는 노드 중 무조건 자신의 부모가 있다는 사실
# 따라서 스택에 넣어두고 값을 확인해야함 

# 스택을 쓸 수 있는 이유는 ? 루트 -> 서브트리이기 때문에 
# 스택은 최근 조상 기억 장치 
# 가장 최근의 값들을 꺼낼 수 있기 때문에 
# 최근 조상부터 거꾸로 확인해야함 