# 사용순서가 주어지면 어떤 것이 중복되어 쓰이는지를 관찰해야함
# 최대 사용하는 전자기기는 계속 꽂아두는게 좋음 
# 이걸 한번한번 셀 것인지 .. 
# 가장 자주 쓰이는걸 그냥 박아두고 .. ?
# 일단 우선순위 큐를 만들고 가장 많이 쓴 애를 자리에 배치하고
    # 원래 입력받은 ]리스트를 순회하면서
        # 값이 같으면 Pass. 
        # 아니면 빼기 이런식
# 위 방법이 안되는게 일단 1,2, n까지는 무조건 배치를 함
    # 배열에서 가장 적게 나오는 애를 교체하는게 현명한 선택 

import sys

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    elecOrder = list(map(int, sys.stdin.readline().split()))

    elecCnt = [0] * (k)

    for i in range(k):
        elecCnt[elecOrder[i] - 1] += 1
    
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
            elecCnt[elecOrder[i] - 1] -= 1
            continue
        
        minIdx = 0
        for idx in range(1, n):
            if (elecCnt[multitap[idx] - 1] <= elecCnt[multitap[minIdx] - 1]):
                minIdx = idx

        multitap[minIdx] = elecOrder[i]
        switchCnt += 1
    
    print(switchCnt)
    

