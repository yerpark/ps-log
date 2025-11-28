import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    sum = 0
    myList = []

    for _ in range(n):
        tmp = int(sys.stdin.readline().strip())
        myList.append(tmp)
        sum += tmp

    myList.sort()

    print(sum // n)
    print(myList[n//2])

    tmpList = [0] * n

    i = 0

    while i < n:
        cnt = 1
        for j in range(i + 1, n):
            if (myList[i] == myList[j]):
                cnt += 1
            else:
                tmpList[i] = cnt
                i = j
                break
    

    print(myList[-1] - myList[0])

