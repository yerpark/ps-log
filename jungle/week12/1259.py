import sys

if __name__ == "__main__":
    
    while (1):
        numberStr = sys.stdin.readline().strip()

        if (numberStr == "0"):
            break
        
        for i in range((len(numberStr) // 2) + 1):
            if (numberStr[i] != numberStr[len(numberStr) - 1 - i]):
                print("no")
                break
        else:
            print("yes")