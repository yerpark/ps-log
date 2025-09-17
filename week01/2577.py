import sys

a = (int)(sys.stdin.readline().strip())
b = (int)(sys.stdin.readline().strip())
c = (int)(sys.stdin.readline().strip())

res = a * b * c

resLine = list(str(res))

for i in range(10) :
    print(f'{resLine.count(str(i))}')