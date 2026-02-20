import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

#약수의 쌍의 성질을 이해해보자
if (n % 2 == 0) :
    print(arr[n//2] * arr[n//2 - 1])
else :
    print(arr[n//2] * arr[n//2])