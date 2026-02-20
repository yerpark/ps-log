import sys


# 시작점을 아무거나 잡아서 
    # 자신과 연결된 애를 다른 집합에 넣기 
    # 반대 집합에 넣으면서 거기에 연결된 애 있는지 체크 
    

if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())

    for _ in range(k):
        v, e = map(int, sys.stdin.readline().split())
        adjList = { i:[] for i in range(1, v + 1) }
        listIdx = [-1] * (v + 1) #초기화 번호를 -1로 지정 
        flag = False
        myStack = []

        for _ in range(e):
            start, dest = map(int, sys.stdin.readline().split())
            adjList[start].append(dest)
            adjList[dest].append(start)
            if (flag == False):
                myStack.append(start)
                listIdx[start] = 1
                flag = True


        flag = False
        #스택이 빌때까지 반복문 돌리기
        # 반복문 처음 들어가면 자기 자식들 다 스택에 넣어주기 
        # 색 칠하기 
        
        while myStack and flag == False:
            cur = myStack.pop()

            for dest in adjList[cur]:
                newIdx = (listIdx[cur] + 1) % 2
                if (listIdx[dest] == -1):
                    listIdx[dest] = newIdx
                    myStack.append(dest)
                elif (listIdx[dest] != newIdx):
                    flag = True
                    break 

        if (flag == True):
            print("NO")
        else:
            print("YES")