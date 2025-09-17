import sys
from itertools import permutations

# 완전 탐색으로 푼다고 하면
# 이것도 도시의 위치를 순열로 나타내고
# 순열을 permutations 사용해서 랜덤 순열로 만들고
# 해당 순열의 비용 계산하는 완전탐색 문제 

n = int(sys.stdin.readline().strip())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
city = [ x for x in range(n) ]

minVal = sys.maxsize

for perm in permutations(city) :
    tmpSum = 0
    for i in range(n - 1) :
        if (arr[perm[i]][perm[i + 1]] == 0) or tmpSum > minVal:
            break 
        tmpSum += arr[perm[i]][perm[i+1]]
    else :
        if (arr[perm[n -1]][perm[0]] == 0) :
            continue
        tmpSum += arr[perm[n-1]][perm[0]]   
        if (tmpSum < minVal) :
            minVal = tmpSum 

print(minVal)