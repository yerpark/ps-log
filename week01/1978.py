import sys
import math

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0

def    checkPrime(num) :
    for i in range(3, math.isqrt(num) + 1, 2) :
        if (num % i == 0) :
            return False
    return True

for i in range(n) :
    if arr[i] == 2 :
        cnt += 1
        continue
    if arr[i] == 1 or arr[i] % 2 == 0 :
        continue
    if checkPrime(arr[i]) == True :
        cnt += 1

print(cnt)