import sys

if __name__ == "__main__":
    m = int(sys.stdin.readline().strip())

    res = 0
    for _ in range(m):
        operation = list(sys.stdin.readline().split())

        if operation[0] == "add":
            res |= (1 << int(operation[1]))
        elif operation[0] == "remove":
            res &= ~(1 << int(operation[1]))
        elif operation[0] == "check":
            if (res & (1 << int(operation[1])) != 0):
                print(1)
            else:
                print(0)
        elif operation[0] == "toggle":
            res ^= (1 << int(operation[1]))
        elif operation[0] == "all":
            res = 0b111111111111111111111
        elif operation[0] == "empty":
            res = 0b000000000000000000000
        
