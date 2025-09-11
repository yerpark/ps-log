import sys

height = [int(sys.stdin.readline()) for x in range(9)]
height.sort()
allHeightSum = sum(height)

breakFlag = False

for i in range(8) :
    if (breakFlag == True) :
        break 
    for j in range(i + 1, 9) :
        if (allHeightSum - height[i] - height[j] == 100) : 
            subtract1 = i
            subtract2 = j
            breakFlag = True

for i in range(9):
    if (i != subtract1 and i != subtract2) :
        print(height[i]) 

