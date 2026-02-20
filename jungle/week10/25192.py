import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    myList = set()
    emojiCnt = 0
    for _ in range(n):
        inputStr = sys.stdin.readline().strip()
        if (inputStr == "ENTER"):
            myList = set()
        elif inputStr not in myList:
            myList.add(inputStr)
            emojiCnt += 1
    
    print(emojiCnt)
