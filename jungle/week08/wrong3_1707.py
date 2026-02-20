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
            # myStack.append(start)

        #스택이 빌때까지 반복문 돌리기
        # 반복문 처음 들어가면 자기 자식들 다 스택에 넣어주기 
        # 색 칠하기 
        # 색 초기화를 항상 같은 색으로 하면-> 탐색 순서에 의해 분리된것도 분리안되었다고 판정할 수 있음
            # ex. 1-> 2-> 3 여기서 2부터 탐색 하고 1로 나중에 돌아오면 1,2 색이 같아서 분리그래프 아닌 것으로 판정 
        # solution -> 자식의 색이 있는 지 확인하고 초기화 
        # 아직 탐색 안한 노드면 자기의 목적지 노드 중에 탐색된 애 있는지 확인하고 인덱스 초기화 
        
        # while myStack and flag == False:
        #     cur = myStack.pop()

        #     if (listIdx[cur] == -1):
        #         listIdx[cur] = 1

        #     for dest in adjList[cur]:
        #         newIdx = (listIdx[cur] + 1) % 2
        #         if (listIdx[dest] == -1):
        #             listIdx[dest] = newIdx
        #             myStack.append(dest)
        #         elif (listIdx[dest] != newIdx):
        #             flag = True
        #             break 


        for i in range(1, v + 1):
            if listIdx[i] == -1:
                myStack.append(i)

                while myStack and flag == False:
                    cur = myStack.pop()

                    if listIdx[cur] == -1:
                        listIdx[cur] = 1

                    for dest in adjList[cur]:
                        newIdx = (listIdx[cur] + 1) % 2
                        if listIdx[dest] == -1:
                            listIdx[dest] = newIdx
                            myStack.append(dest)
                        elif listIdx[dest] != newIdx:
                            flag = True
                            break
                if flag:
                    break

        if (flag == True):
            print("NO")
        else:
            print("YES")