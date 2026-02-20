# -의 왼쪽을 최소로 만들어야 함
# -의 오른쪽을 최대로 만들어야 함

# -가 나타나면 오른쪽에 -없는지 확인
    # 있으면 - 나타날때까지 괄호치기
    # 없으면 전체 괄호

import sys

if __name__ == "__main__":
    inputStr = sys.stdin.readline().strip()

    minusSplit = list(inputStr.split('-'))
    arr = []
    minSum = 0
    for i in range(len(minusSplit)):
        tmpArr = list(map(int, minusSplit[i].split('+')))
        arr.append(tmpArr)
        if i == 0:
            minSum = sum(tmpArr)
        else:
            minSum -= sum(tmpArr)

    print(minSum)
    

