import sys

n = int(sys.stdin.readline().strip())

rowUsed = [False] * n
diag1Used = [False] * 2 * n # /
diag2Used = [False] * 2 * n # \

def recursive_nqueen(currCol) :

    if (currCol == n) :
        return 1

    for currRow in range(n) :
        if rowUsed[currRow] or diag1Used[currCol - currRow + n] or diag2Used[currCol + currRow] :
            return 0
        rowUsed[currRow] = True
        diag1Used[currCol - currRow + n] = True
        diag2Used[currCol + currRow] = True
        cnt = recursive_nqueen(currCol + 1)
        rowUsed[currRow] = False
        diag1Used[currCol - currRow + n] = False
        diag2Used[currCol + currRow] = False
    
    return (cnt)

print(recursive_nqueen(0))
        