import sys

n = int(sys.stdin.readline().strip())
list = []

for i in range(n):
    val = int(sys.stdin.readline().strip())
    for j in range(len(list) - 1, -1, -1):
        if (val >= list[j]) :
            list.pop()
        else :
            break
    list.append(val)

print(len(list))
