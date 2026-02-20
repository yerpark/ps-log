def binary_search(piles, target):
    left, right = 0, len(piles) - 1
    while left <= right:
        mid = (left + right) // 2
        if piles[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def length_of_lis(arr):
    piles = []
    for num in arr:
        idx = binary_search(piles, num)
        if idx == len(piles):
            piles.append(num)
        else:
            piles[idx] = num
    return len(piles)

# 입력 처리
n = int(input())
arr = list(map(int, input().split()))
print(length_of_lis(arr))
