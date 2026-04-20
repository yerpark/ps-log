# dfs? 최소 비교?
# 팀이 2개니까 팀을 나누고 해당 경우의 능력 계산

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    powers = []
    for _ in range(n):
        tmp = list(map(int, sys.stdin.readline().split()))
        powers.append(tmp)

    isStartTeam = [False] * n
    startTeamCnt = 0
    minDiff = [float("INF")]

    # 어떤 팀인지는 중요하지 않음.
    # 임의로 스타트 팀에 들어갈 N/2 조합을 구해도 괜찮음
    # 근데 이걸 어떻게 구하지
    # 재귀로 구하기 -> 이 방향으로 구하는 것
    # 반복문을 도는데 i번째 타임이오면 i-n-1까지의 조합만 있는 것

    def getDiff():
        startTeamSum = 0
        linkTeamSum = 0

        for i in range(n):
            for j in range(i, n):
                if i == j or isStartTeam[i] != isStartTeam[j]:
                    continue
                if isStartTeam[i] and isStartTeam[j]:
                    startTeamSum += powers[i][j] + powers[j][i]
                elif not isStartTeam[i] and not isStartTeam[j]:
                    linkTeamSum += powers[i][j] + powers[j][i]

        return abs(startTeamSum - linkTeamSum)

    def dfs(i, startTeamCnt):
        if startTeamCnt == n // 2:
            minDiff[0] = min(minDiff[0], getDiff())
            return

        if (n - i) < ((n // 2) - startTeamCnt):
            return

        isStartTeam[i] = True
        dfs(i + 1, startTeamCnt + 1)
        isStartTeam[i] = False
        dfs(i + 1, startTeamCnt)

    # ---
    dfs(0, 0)
    print(minDiff[0])
