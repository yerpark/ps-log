# 전략 : str으로 바꿔서 보자
# 0~9가 몇번 등장하는지를 배열에 저장
# 9부터 소진하면서 숫자 완성
# ex. 9 3개 있으면 -> 999877이렇게 완성하게


def solution(X, Y):
    str_X = str(X)
    str_Y = str(Y)
    arr_X = [0] * 10  # 각각의 숫자 출현수를 셀 배열
    arr_Y = [0] * 10  # 각각의 숫자 출현수를 셀 배열

    for i in range(len(str_X)):
        arr_X[int(str_X[i])] += 1

    for i in range(len(str_Y)):
        arr_Y[int(str_Y[i])] += 1

    res = 0
    cnt = 0
    for i in range(9, -1, -1):
        while arr_X[i] != 0 and arr_Y[i] != 0:
            res = res * 10 + i
            arr_X[i] -= 1
            arr_Y[i] -= 1
            cnt += 1

    if cnt == 0:
        res = -1
    answer = str(res)

    return answer


if __name__ == "__main__":
    print(solution(100, 2345))  # "-1"
    print(solution(100, 203045))  # "0"
    print(solution(100, 123450))  # "10"
    print(solution(12321, 42531))  # "321"
    print(solution(5525, 1255))  # "552"
