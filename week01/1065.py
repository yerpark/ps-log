import sys

n = int(sys.stdin.readline().strip())


if n >= 100 :
    sum = 99 #한자리수, 두자리수 수 다 더해두기

    for num in range(101, n + 1) :
        tmpList = []
        while (num != 0) :
            tmpList.append(num % 10)
            num //= 10
        diff = tmpList[0] - tmpList[1]
        for i in range(1, len(tmpList) - 1) :
            if (tmpList[i] - tmpList[i + 1] != diff) :
                break
        else :
            sum += 1

    print (sum)
else :
    print (n)