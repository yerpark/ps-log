import sys
sys.setrecursionlimit(10**7)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    pairs = [ [arr[i], i] for i in range(n)]

    pairs.sort()

    result = [0] * n 

    rank = 0
    result[pairs[0][1]] = 0

    for i in range(1, n):
        if pairs[i - 1][0] != pairs[i][0]:
            rank += 1
        result[pairs[i][1]] = rank
    
    print(" ".join(map(str, result)))

    