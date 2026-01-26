# 가장 넓이가 큰 직사각형을 구해야 함
# 높이를 탐색하면서 가장 큰 값을 구하기
# 1은 직사각형의 개수..
# 2는 다음 사각형이 자신이랑 같거나 클때까지 계속 구할 수 있음. 작은 애 만나면 max 저장해두고 초기화


import sys

if __name__ == "__main__":
    while 1:
        arr = list(map(int, sys.stdin.readline().split()))
        n = arr[0]
        if n == 0:
            break
        heights = arr[1:]

        maxHeight = max(heights)
        max_heights_each = [0] * (maxHeight + 1)
        max_heights_each[1] = n

        for i in range(1, maxHeight + 1):
            cnt = 0
            tmp_max = 0
            for j in range(n):
                if heights[j] >= i:
                    cnt += 1
                else:
                    tmp_max = max(tmp_max, cnt * i)
                    cnt = 0

            max_heights_each[i] = max(tmp_max, max_heights_each[i])

        print(max(max_heights_each))
