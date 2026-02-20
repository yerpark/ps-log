import sys

inputStr = sys.stdin.readline().strip()
spaceFlag = 0
wrdCnt = 0

for i in range(len(inputStr)) :
    if (inputStr[i] == " " and i != 0) :
        if (spaceFlag == 0) :
            spaceFlag = 1
            wrdCnt += 1
    else :
        spaceFlag = 0

if (inputStr != "" and spaceFlag == 0) :
    wrdCnt += 1

print (wrdCnt)