import sys

n = 0
d = 0
k = 0
c = 0
sushi = []

def get_sushi_cnt(coupon):
    tmp_max_cnt = 0
    arr = []
    arr.append(sushi[coupon])
    
    for i in range(1, k + 1):
        arr.append(sushi[(coupon - i) % n])
    
    mySet = set(arr)
    tmp_max_cnt = max(tmp_max_cnt, len(mySet))
    arr = []
    arr.append(sushi[coupon])
    
    for i in range(1, k + 1):
        arr.append(sushi[(coupon + i) % n])
    
    mySet = set(arr)
    tmp_max_cnt = max(tmp_max_cnt, len(mySet))
    return tmp_max_cnt

if __name__ == "__main__":
    n, d, k, c = map(int, sys.stdin.readline().split())
    coupon_idx = []
    sushi = []

    for i in range(n):
        sushi.append(int(sys.stdin.readline().strip()))
        if (sushi[-1] == c):
            coupon_idx.append(i)

    max_cnt = 0
    
    for coup in coupon_idx:
        tmp_cnt = get_sushi_cnt(coup)
        
        if (k <= max_cnt):
            max_cnt = max(tmp_cnt, max_cnt)

        if (k < max_cnt):
            break 
    
    if (k <= max_cnt):
        print(max_cnt)
    else:
        # 배열 순회하면서 연속개수 확인하는 방식
        