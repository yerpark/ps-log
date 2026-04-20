# 어떻게 확률 정보를 관리할 것인지?
# list 배열에다가 국가명(string), 확률 다 넣을지?
# 아니면 index 기반으로 n*n 배열을 만들 것인지?

# 다음라운드에 진출할 확률이라는 것은?
# 6경기 후에 상위 2팀이 될 확률
# 승점이 탑2거나 아니면 랜덤 확률에서 승리하거나

# 그럼 dfs로 모든 확률 탐구를 해야하나?
# 이기는 경우, 안이기는 경우..
# 그래서 비교?

# 3 * 3 * 3 * 3 * 3 * 3의 경우의 수가 있음
# 근데 각각의 확률을 예측을 해야함..

import sys

if __name__ == "__main__":
    participants = list(sys.stdin.readline().split())
    participants_index = {x: i for i, x in enumerate(participants)}

    odds = {participant: {} for participant in participants}
    for i in range(6):
        tmp_list = list(sys.stdin.readline().split())
        participant = tmp_list[0]
        opponent = tmp_list[1]
        tmp_list = list(map(float, tmp_list[2:]))
        odds[participant] = {opponent: tmp_list}
        tmp_list.reverse()
        odds[opponent] = {participant: tmp_list}

    print(odds)
