import sys

NUM_MAX = 2000000

def is_palindrome(number):
    
    tmp = str(number)
    for i in range(len(tmp) // 2):
        if (tmp[0 + i] != tmp[len(tmp) - 1 -i]):
            return False
    return True

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    prime_number = [True] * (NUM_MAX + 1)
    prime_number[0] = False
    prime_number[1] = False

    if (n == 1 or n == 2):
        print(2)
    else:
        i = 2
        for j in range(i * i, (NUM_MAX + 1), i):
            prime_number[j] = False
        
        for i in range(3, (NUM_MAX + 1), 2):
            if prime_number[i] == True:
                for j in range(i * i, (NUM_MAX + 1), i):
                    prime_number[j] = False

                if n <= i and is_palindrome(i) == True:
                    print(i)
                    break 

