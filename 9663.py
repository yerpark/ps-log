import sys

n = int(input())

rowUsed = [False] * n
diag1Used = [False] * 2 * n
diag2Used = [False] * 2 * n

# def no_conflict(currRow, currCol):
#     if rowUsed[currRow] == True :
#         return False
#     elif diag1Used[(currCol - currRow + n - 1)] == True :
#         return False
#     elif diag2Used[(currCol + currRow)] == True :
#         return False
#     return True

# n *n 에서 n * (n-1)으로 가는 것 . . 
def recursive_nqueen(currCol, n) :
    if (currCol == n) :
        return (1)

    res = 0
    for currRow in range((n)) :
        if rowUsed[currRow] or diag1Used[currCol - currRow + n - 1] or diag2Used[currCol + currRow] :
            continue
        else :
            rowUsed[currRow] = True
            diag1Used[(currCol - currRow + n - 1)] = True
            diag2Used[(currCol + currRow)] = True
            res += recursive_nqueen(currCol + 1, n)

            rowUsed[currRow] = False
            diag1Used[(currCol - currRow + n - 1)] = False
            diag2Used[(currCol + currRow)] = False

    return (res)

print (recursive_nqueen(0, n)) 