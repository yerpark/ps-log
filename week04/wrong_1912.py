import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    maxSubArraySum = max(max(arr), sum(arr))

    for subArrayLen in range(2, n):
        currLevelMax = sum(arr[0:subArrayLen])
        tmpSum = currLevelMax

        for i in range(subArrayLen, n):
            tmpSum = tmpSum - arr[i - subArrayLen] + arr[i]
            if (tmpSum > currLevelMax):
                currLevelMax = tmpSum
        
        if (maxSubArraySum < currLevelMax):
            maxSubArraySum = currLevelMax

    print(maxSubArraySum)