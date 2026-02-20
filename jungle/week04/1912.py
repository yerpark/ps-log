import sys

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))

    tmpSum = arr[0]
    maxSubArraySum = arr[0]
    for i in range(1, n):
        tmpSum = max(tmpSum + arr[i], arr[i])
        maxSubArraySum = max(tmpSum, maxSubArraySum)
    
    print(maxSubArraySum)