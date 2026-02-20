import sys

n = 0
minResult = float('inf')
maxResult = float('-inf')
numbers = []
operators = []
visited = []

def operate(operator, a, b):
    if (operator == '+'):
        return a + b
    elif (operator == '-'):
        return a - b
    elif (operator == '*'):
        return a * b
    else:
        if a < 0:
            return -1 * ((-1 * a) // b)
        return a // b

def dfs(i, result):
    global minResult, maxResult, numbers, operators, visited
    if (i == n - 1):
        minResult = min(minResult, result)
        maxResult = max(maxResult, result)
        return 

    for j in range(n - 1):
        if (visited[j] == False):
            visited[j] = True
            tmpResult = operate(operators[j], result, numbers[i + 1])
            dfs(i + 1, tmpResult)
            visited[j] = False
            

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().split()))
    tmp = list(map(int, sys.stdin.readline().split()))
    operators = []

    for _ in range(tmp[0]):
        operators.append('+')
    for _ in range(tmp[1]):
        operators.append('-')
    for _ in range(tmp[2]):
        operators.append('*')
    for _ in range(tmp[3]):
        operators.append('//')

    visited = [False] * len(operators)

    dfs(0, numbers[0])

    print(maxResult)
    print(minResult)