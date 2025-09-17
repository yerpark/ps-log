import  sys
import  math

isPrime = [True] * 1000001

def eratosthenes_sieve(n):
    isPrime[0] = isPrime[1] = False
    for i in range(2, math.isqrt(n) + 1) :
        if isPrime[i] == True :
            for j in range (i * i, n + 1, i) :
                isPrime[j] = False

def getPartition(num) :
    val1 = val2 = num // 2

    while (True) :
        if isPrime[val1] and isPrime[val2]:
            print(f"{val1} {val2}")
            return True
        else :
            val1 -= 1
            val2 += 1

n = int(sys.stdin.readline().strip())
inputVal = [int(sys.stdin.readline().strip()) for _ in range(n)]
eratosthenes_sieve(1000000)

for i in range(n) :
    getPartition(inputVal[i])
        