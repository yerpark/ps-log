import sys

def partitionRectangle(arr, resList, n, row, col):
    standard = arr[row][col]
    myFlag = False
    for currRow in range(row, row + n):
        for currCol in range(col, col + n):
            if (standard != arr[currRow][currCol]):
                myFlag = True
                partitionRectangle(arr, resList, n//2, row, col)
                partitionRectangle(arr, resList, n//2, row, col + n//2)
                partitionRectangle(arr, resList, n//2, row + n//2, col)
                partitionRectangle(arr, resList, n//2, row + n//2, col + n//2)
                break
        if (myFlag == True):
            break
    else :
        if (standard == 0): #하얀색
            resList[0] += 1
        else: #파란색 
            resList[1] += 1
            

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

    resList = [0, 0]

    partitionRectangle(arr, resList, n, 0, 0)

    print(resList[0])
    print(resList[1])


