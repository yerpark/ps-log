# 재귀로 풀라고 했으니까 재귀로 
# base case 찾았으니까 n * n 일때 쪼개서 
# n * n 의 케이스는 사실상 n -1 * n -1 사각형 배치의 케이스와 그에 따라 놓을 수 있는 1개의 queen 위치 

import sys

n = int(sys.stdin.readline().strip())

def recursive_nqueen(num) :
    if num == 1 :
        return 1
    elif num == 2 or num == 3 :
        return 0
    elif num == 4 :
        return 2 
    else :
        return 4 * recursive_nqueen(num - 1)

print (recursive_nqueen(n))