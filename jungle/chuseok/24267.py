import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    sum = 0
    for a in range(n - 2, 0, -1):
        sum += ((a + 1) * a) // 2

    print(sum)
    print(3)