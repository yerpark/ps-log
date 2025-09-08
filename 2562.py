import sys

max_val = 0 
max_idx = 0

for i in range(9) :
    tmp = (int)(sys.stdin.readline().strip())
    if (max_val < tmp) :
        max_val = tmp
        max_idx = i + 1

print(max_val)
print(max_idx)
