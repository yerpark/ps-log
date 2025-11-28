import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    infoList = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

    for i in range(n):
        cnt = 0
        for j in range(n):
            if (i != j and \
                infoList[j][0] > infoList[i][0] \
                    and infoList[j][1] > infoList[i][1]):
                cnt += 1
        print(f"{cnt + 1} ", end="")
