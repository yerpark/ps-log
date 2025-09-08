import sys

def recursive_factorial(num) :
    if (num == 0 or num == 1) :
        return (1)
    else :
        return (num * recursive_factorial(num - 1))
    
n = int(sys.stdin.readline().strip())
print (recursive_factorial(n))
