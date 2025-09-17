import sys
from itertools import permutations 

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

max = 0
for perm in permutations(arr) :
    tmpSum = 0
    for i in range(n - 1):
        tmpSum += abs(perm[i] - perm[i + 1])
    if (tmpSum > max) :
        max = tmpSum

print(max)