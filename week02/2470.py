# MAIN IDEA : 알칼리성 리스트의 원소들을 순회하면서, 
#             해당 값의 절대값과 가까운 값이 있는지 산성 리스트에서 이분탐색

import  sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    inputVal = list(map(int, sys.stdin.readline().split()))

    acidicList = [x for x in inputVal if x > 0]
    alkalineList = [x for x in inputVal if x < 0]

    acidicList.sort()
    alkalineList.sort()

    if (len(acidicList) == 0):
        print(f"{alkalineList[-2]} {alkalineList[-1]}")
    elif (len(alkalineList) == 0):
        print(f"{acidicList[0]} {acidicList[1]}")
    else :
        minSum = 2000000001
        min1, min2 = 0, 0
        if (len(acidicList) >= 2):
            minSum = acidicList[0] + acidicList[1]
            min1 = acidicList[0]
            min2 = acidicList[1]
        if (len(alkalineList) >= 2 and minSum >= abs(alkalineList[-1] + alkalineList[-2])):
            minSum = abs(alkalineList[-1] + alkalineList[-2])
            min1 = alkalineList[-2]
            min2 = alkalineList[-1]
        for a in alkalineList:
            
            #이분탐색 
            startIdx = 0
            endIdx = len(acidicList) - 1

            while (startIdx <= endIdx):
                midIdx = (startIdx + endIdx) // 2

                if (abs(acidicList[midIdx] + a) > minSum):
                    if ((acidicList[midIdx] + a) < 0):
                        startIdx = midIdx + 1
                    else:
                        endIdx = midIdx - 1
                else:
                    minSum = abs(acidicList[midIdx] + a)
                    min2 = acidicList[midIdx]
                    min1 = a
                    if ((acidicList[midIdx] + a) < 0):
                        startIdx = midIdx + 1
                    else:
                        endIdx = midIdx - 1
            
            if (minSum == 0):
                break
        
        print(f"{min(min1, min2)} {max(min1, min2)}")
