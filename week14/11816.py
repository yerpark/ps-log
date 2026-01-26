import sys

def octalToDecimal(numStr):
    res = 0
    octalMultiplier = 1
    for i in range(len(numStr) - 1, 0, -1):
        res += octalMultiplier * (int(numStr[i]))
        octalMultiplier *= 8

    return res

def hexaTranslator(alphabet):
    if (alphabet == "a"):
        return 10
    elif (alphabet == "b"):
        return 11
    elif (alphabet == "c"):
        return 12
    elif (alphabet == "d"):
        return 13
    elif (alphabet == "e"):
        return 14
    elif (alphabet == "f"):
        return 15
    elif (int(alphabet) != 0):
        return int(alphabet)
    else:
        return 0

def hexaToDecimal(numStr):
    res = 0
    octalMultiplier = 1
    for i in range(len(numStr) - 1, 1, -1):
        res += octalMultiplier * (hexaTranslator(numStr[i]))
        octalMultiplier *= 16

    return res

if __name__ == "__main__":
    numStr = sys.stdin.readline().strip()

    
    if (numStr[0] == "0" and numStr[1] == "x"):
        print(hexaToDecimal(numStr))
    elif (numStr[0] == "0"):
        print(octalToDecimal(numStr))
    else:
        print(numStr)