import sys

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    monsters_alphabet = {}
    monsters_numeric  = {}
    for i in range(1, n + 1):
        monster = sys.stdin.readline().strip()
        monsters_alphabet[monster] = i
        monsters_numeric[i] = monster

    for _ in range(m):
        inputStr = sys.stdin.readline().strip()
    
        if (inputStr.isdigit()):
            val = int(inputStr)
            print(monsters_numeric[val])
        else:
            print(monsters_alphabet[inputStr])
            
