import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    numStr = sys.stdin.readline().strip()

    total = 0
    for i in range(n):
        total += int(numStr[i])
    # 너구리 says: 위의 3줄을 아래 한줄로 변경 가능
    # total = sum(map(int, numStr))
        # map(함수, iterable)
            # iterable 안의 모든 요소에 함수를 적용해서 새로운 iterator를 만들어라  
    
    print(total)