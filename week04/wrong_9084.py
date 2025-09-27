#첫번째 인자로 나누어질 수 있으면 무조건 1
#작은수로 올라가면서 경우의 수 확정

import sys

def getMinCnt(currIdx, coins, targetVal):

    if (targetVal in minCntArr):
        if (currIdx in minCntArr[targetVal]):
            return minCntArr[targetVal][currIdx]
    
    if (currIdx == 0):
        if( targetVal % coins[currIdx] == 0):
            minCntArr[targetVal] = {}
            minCntArr[targetVal][currIdx] = 1
            return (1)
        else:
            return (0)
    
    res = 0
    
    for currCoinUse in range((targetVal // coins[currIdx]) + 1):
        if (currIdx - 1 >= 0):
            res += getMinCnt(currIdx - 1, coins, targetVal - (currCoinUse * coins[currIdx]))
    
    return res


if __name__ == "__main__":

    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        coins = list(map(int, sys.stdin.readline().split()))
        targetVal = int(sys.stdin.readline().strip())

        global minCntArr 
        minCntArr = {} #구조 : key -> 값 (가치)
                       #      val -> {key -> coin : val -> 경우의 수 } 

        print(getMinCnt(n - 1, coins, targetVal))
            