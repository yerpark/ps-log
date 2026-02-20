# 정답인 h 자체를 이분탐색으로 

import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start_h = 0
end_h = max(trees)
max_h = -1

while (start_h <= end_h):
    mid_h = (start_h + end_h) // 2
    tmp_sum = 0

    for tree in trees :
        if (mid_h < tree) :
            tmp_sum += tree - mid_h
        
    if (tmp_sum >= m):
        start_h = mid_h + 1
        max_h = max(mid_h, max_h)
    else :
        end_h = mid_h - 1

print (max_h)