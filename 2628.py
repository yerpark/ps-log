import sys

col, row = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline().strip())

colSplitVal = [0]
rowSplitVal = [0]

for _ in range(t) :
    typeVal, boxIdx = map(int, sys.stdin.readline().split())
    if (typeVal == 1) :
        colSplitVal.append(boxIdx)
    else :
        rowSplitVal.append(boxIdx)

colSplitVal.append(col)
rowSplitVal.append(row)

colSplitVal.sort()
rowSplitVal.sort()

newColLen = []
newRowLen = []

for i in range(len(colSplitVal) - 1) :
    newColLen.append(colSplitVal[i + 1] - colSplitVal[i])

for i in range(len(rowSplitVal) - 1) :
    newRowLen.append(rowSplitVal[i + 1] - rowSplitVal[i])

max = 0
for row in (newRowLen) :
    for col in (newColLen) :
        if (row * col > max) :
            max = row * col

print (max)