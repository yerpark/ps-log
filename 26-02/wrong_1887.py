#정렬을 한번 해서 새로운 배열을 만들기 
#원배열을 보면서 정렬된 배열 어디에 있는지 확인

import sys, copy

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))

    sorted_set = sorted(set(arr))

    for a in arr:
        for i in range(len(sorted_set)):
            if sorted_set[i] == a:
                print(i, end=" ")
                break