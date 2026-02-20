import sys

if __name__ == "__main__":
    l = int(sys.stdin.readline().strip())
    inputStr = sys.stdin.readline().strip()
    r = 31
    m = 1234567891
    sum = 0
    power = 1

    for i in range(len(inputStr)):
        tmp = ord(inputStr[i]) - ord('a') + 1
        tmp *= power
        sum += tmp
        power *= r

    print(sum % m)