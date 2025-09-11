import sys

n, row, col = map(int, sys.stdin.readline().split())

def recursive_z(n, stepAhead, row, col) :
    midBound = pow(2, n - 1)
    endBound = pow(2, n)

    if (0 <= col and col < midBound) and (0 <= row and row < midBound) :
        stepAhead += 0
    elif (midBound <= col and col < endBound) and (0 <= row and row < midBound) :
        stepAhead += midBound * midBound
        col -= midBound
    elif (0 <= col and col < midBound) and (midBound <= row and row < endBound) :
        stepAhead += 2 * midBound * midBound
        row -= midBound
    else :
        stepAhead += 3 * midBound * midBound
        row -= midBound
        col -= midBound

    if (n == 1) :
        return (stepAhead)
    else : 
        return (recursive_z(n - 1, stepAhead, row, col))
    
print (recursive_z(n, 0, row, col))

# note
    # step에만 집중해서 row, col을 갱신하지 않고 그냥 넘겼다가 처음에 틀림
    # 어찌되었건 작은 사각형으로 만들기 위해서는 작은 사각형 안에서 row, col이 해석될 수 있도록 만들어줘야 함 (좌표재조정)
