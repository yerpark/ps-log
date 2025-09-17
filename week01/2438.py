import sys

n = int(sys.stdin.readline().strip())

for i in range(1, n + 1) :
    for _ in range(i) :
        print('*',end="")
    print("")