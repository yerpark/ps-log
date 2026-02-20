import sys
from collections import defaultdict

n,d,k,c = map(int, sys.stdin.readline().split())
sushi = [ int(sys.stdin.readline().strip()) for _ in range(n) ]

count = defaultdict(int)
unique = 0
max_cnt = 0

for i in range(k):
    if count[sushi[i]] == 0:
        unique += 1
    count[sushi[i]] += 1

max_cnt = unique + (1 if count[c] == 0 else 0)

for i in range(1, n):
    prev = sushi[i - 1]
    count[prev] -= 1
    if count[prev] == -1:
        unique -= 1

    next_sushi = sushi[(i + k - 1) % n]
    if count[next_sushi] == 0:
        unique += 1
    count[next_sushi] += 1

    curr_max = unique + (1 if count[c] == 0 else 0)
    max_cnt = max(max_cnt, curr_max)

print (max_cnt)