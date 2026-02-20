import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    arr_a = list(map(int, sys.stdin.readline().split()))
    arr_b = list(map(int, sys.stdin.readline().split()))

    arr_a.sort()
    arr_b.sort()

    cnt_a = n
    cnt_b = m

    i = 0
    j = 0

    while (i < n and j < m):
        if (arr_a[i] == arr_b[j]):
            i += 1
            j += 1
            cnt_a -= 1
            cnt_b -= 1
        elif (arr_a[i] > arr_b[j]):
            j += 1
        else:
            i += 1
    
    print(cnt_a + cnt_b)
