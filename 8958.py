import sys

n = (int)(sys.stdin.readline().strip())

for _ in range(n) :
    str = sys.stdin.readline().strip()
    currScore = 0
    finalScore = 0
    for i in range (len(str)):
        if (str[i] == 'O') :
            currScore += 1
        else :
            currScore = 0
        finalScore += currScore
    print(finalScore)