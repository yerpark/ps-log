import sys

sys.setrecursionlimit(10 ** 6)

def getCnt(i, j):

    if (i < 0 or j < 0):
        return 0
    
    if (i == 0 and j == 0 and str1[i] != str2[i]):
        return 0

    if (str1[i] == str2[j]):
        return 1 + getCnt(i - 1, j - 1)
    else:
        return max(getCnt(i, j - 1), getCnt(i - 1, j))

if __name__ == "__main__":
    global str1
    str1 = sys.stdin.readline().strip()
    global str2
    str2 = sys.stdin.readline().strip()

    print(getCnt(len(str1) - 1, len(str2) - 1))
