import sys


if __name__ == "__main__" :
    k = int(sys.stdin.readline().strip())

    myList = []

    for _ in range(k):
        inputVal = int(sys.stdin.readline().strip())
        if (inputVal != 0) :
            myList.append(inputVal)
        else :
            myList.pop()
    
    print(sum(myList))
