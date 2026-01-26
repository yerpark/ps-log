import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    if (n == 1):
        sys.exit()

    i = 2
    original_number = n
    while (i * i <= original_number):
        if (n % i == 0):
            print(i)
            n //= i
        else:
            i += 1
    
    if (n != 1):
        print(n)
    
