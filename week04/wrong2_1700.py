
import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    elecOrder = list(map(int, sys.stdin.readline().split()))
    
    multitap = [elecOrder[0]]
    curr = 0
    while (len(multitap) != n):
        if (k <= curr):
            break
        if (elecOrder[curr] not in multitap):
            multitap.append(elecOrder[curr])
        curr += 1
    
    switchCnt = 0

    for i in range (curr, k):
        if elecOrder[i] in multitap:
            continue
        
        hasToBeSwitchedIdx = 0
        for j in range(i + 1, k):
            for idx in range(n):
                if (elecOrder[j] == multitap[idx]):
                    hasToBeSwitchedIdx = idx + 1
                    break

        multitap[hasToBeSwitchedIdx] = elecOrder[i]
        switchCnt += 1
    
    print(switchCnt)
    

