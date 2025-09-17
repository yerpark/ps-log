
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

    while (start != end):
        mid = (start + end) // 2
        if ((start + end) % 2 != 0) :
            mid += 1

        if (arr[mid] == val) :
            return True
        elif (arr[mid] < val) :
            start = mid
        else :
            end = mid

        if mid == start or mid == end : #여기서 위에서 인덱스 재조정한 것들이 다 걸리는 문제 발생 
            if (arr[start] == val or arr[end] == val) :
                return True
            else :
                return False 

    return False

for i in range(m) :
    if (checkIfValExist(checkVal[i], 0, n-1) == True):
        print(1)
    else :
        print (0)

# note
    # 무한루프 방지에 대해서 연구필요
    # 현재는 하드 코딩으로 막았는데, 이분탐색을 설계할때부터 무한루프를 방지하는 방법 고안 필요

