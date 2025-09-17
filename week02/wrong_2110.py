import sys

n, c = map(int, sys.stdin.readline().split())
house = [ int(sys.stdin.readline().strip()) for _ in range(n) ]
settedIdx = []

house.sort()

#첫번째 원소와 두번째 원소에 공유기 설치
settedIdx.append(0)
settedIdx.append(n - 1)

def settingAtMiddle(start, end, remaining) :
    mid = (start + end) // 2

    if (remaining > 1):
        settingAtMiddle(start, mid - 1, remaining // 2)
        settingAtMiddle(mid + 1, end, remaining // 2)
    else :
        settedIdx.append(mid)

settingAtMiddle(0, n - 1, c - 2)

settedIdx.sort()

minLen = 1000000000
for i in range(len(settedIdx) - 1) :
    tmpLen = house[settedIdx[i + 1]] - house[settedIdx[i]]
    minLen = min(minLen, tmpLen)

print(minLen)

#🎯 힌트 (한 문장):

#넌 좌표 간격을 기준으로 풀어야 할 문제를, 인덱스 간격으로 풀고 있다.