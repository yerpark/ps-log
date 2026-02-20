# 부분 수열
#     원래 순서 유지해야함
#     건너뛰기 가능
#     공집합 포함
#     자기 자신도 포함

# 문제 접근 계획
    # - 길이로 이분탐색 

    # - 만약 해당 길이를 만족하는 부분수열이 있는가?
    #     - 있다면 True 리턴, 길이 출력
    #     - 없다면 길이 재조정 -> min 길이도 업데이트 
    #     - 해당 길이를 만족하는 부분 수열이 있는지 확인하는 방법
    #         - 특정 조건 "증가해야 함;이전 원소는 앞의 원소보다 작아야 함" 을 만족하면 바로 배치
    #         - {10, 20, 10, 30, 15, 30, 50} 같은 경우가 우려되긴 하지만 일단 고 
                # 정확히 이 부분 때문에 틀림
                # 그니까 최소 n 만족하는 경우를 어떻게 할 것인지에 대한 고민 . 지금은 순차적으로 보고 다른 경우를 생각 X 
import sys
# from function_visualizer import FunctionVisualizer
sys.setrecursionlimit(10**6)

# visualizer = FunctionVisualizer()


def isLenBuildable(len, arr, n):

    global cache
    cache = {}

    for firstIdx in range(n):
        count = 1
        if (isLenBuildableRecursive(len, arr, firstIdx, n, count) + count >= len):
            return (True)
    
    return (False)

# @visualizer.visualize()
def isLenBuildableRecursive(len, arr, firstIdx, n, count):
    key = firstIdx
    if key in cache:
        return cache[key]
    
    res = 0
    
    for currIdx in range(firstIdx + 1, n):
        if (n - currIdx < len - count):
            return 0
        if (arr[firstIdx] < arr[currIdx]):
            res = 1
            if (res + count >= len):
                break
            else:
                res += isLenBuildableRecursive(len, arr, currIdx, n, count + 1)
                if (res + count >= len):
                    break
    
    cache[firstIdx] = res
    return (res)


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))

    leftLen = 0
    rightLen = len(arr)
    maxLen = -1 #불가능한 값으로 초기화

    if (n == 1):
        print(1)
    else:
        while (leftLen <= rightLen):
            midLen = (leftLen + rightLen) // 2
            
            if (isLenBuildable(midLen, arr, n) == True):
                maxLen = max(maxLen, midLen)
                leftLen = midLen + 1
            else:
                rightLen = midLen - 1

        print(maxLen)
    
    # visualizer.render("isLenBuildableRecursive", "png")