
# 자연수의 배열에서 특정 수가 있는지 없는지 찾아서 bool 리턴하는 함수 짜기
    # 이분탐색으로 하려면 기본 조건은 정렬을 할 것임
    # 정렬을 한 후에 이분탐색을 하는 함수를 실행시키면 됨 

import  sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().strip())
checkVal = list(map(int, sys.stdin.readline().split()))

arr.sort()

def checkIfValExist(val, start, end) :

    while (start <= end): #원래 start!=end -> start == end인 경우도 있음 
        mid = (start + end) // 2
        
        if (arr[mid] == val) :
            return True
        elif (arr[mid] < val) :
            start = mid + 1 # 
        else :
            end = mid - 1

    return False

for i in range(m) :
    if (checkIfValExist(checkVal[i], 0, n-1) == True):
        print(1)
    else :
        print (0)

# note
    # 무한루프 방지에 대해서 연구필요
    # 현재는 하드 코딩으로 막았는데, 이분탐색을 설계할때부터 무한루프를 방지하는 방법 고안 필요
        # start, end 위치 재조정을 