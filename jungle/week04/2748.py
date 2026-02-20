import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    
    arr = [0, 1]

    for i in range(2, n + 1):
        arr.append(arr[i - 2] + arr[i - 1])
    
    print(arr[n])