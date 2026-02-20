#스택 3개 생성
    # 스택 1개는 입력 받으면서 수신하는 탑 있는지 체크하는 용
    # 복원용 스택 하나 만들어서 자기보다 작은 애들 담기 
    # 결과 출력용 스택 1개

# 시간초과 

import sys

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    stackToUse = list(map(int, sys.stdin.readline().split()))
    stackToRestore = []
    stackToPrint = []

    while (stackToUse):
        cur = stackToUse.pop()
        receptionTower = 0

        while (stackToUse):
            if (stackToUse[-1] >= cur):
                receptionTower = len(stackToUse)
                break
            
            stackToRestore.append(stackToUse.pop())

        stackToPrint.append(receptionTower)

        while (stackToRestore):
            stackToUse.append(stackToRestore.pop())
    
    while (stackToPrint):
        print(f"{stackToPrint.pop()} ", end="")
