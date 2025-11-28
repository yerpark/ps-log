import sys

def lowerbound(target, arr, start, end):
    while (start < end):
        mid = (start + end) // 2
        if (arr[mid] < target):
            start = mid + 1
        else:
            end = mid
    return start

def upperbound(target, arr, start, end):
    while (start < end):
        mid = (start + end) // 2
        if (arr[mid] <= target):
            start = mid + 1
        else:
            end = mid
    return start 

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    cardList = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline().strip())
    numList = list(map(int, sys.stdin.readline().split()))

    cardList.sort()

    for num in numList:
        cnt = upperbound(num, cardList, 0, n) - lowerbound(num, cardList, 0, n)
        print(f"{cnt} ", end="")