import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    inputList = [ sys.stdin.readline().strip() for _ in range(n) ]
    cnt = 0

    for _ in range(m):
        tmp = sys.stdin.readline().strip()
        if tmp in inputList:
            cnt += 1

    print(cnt)