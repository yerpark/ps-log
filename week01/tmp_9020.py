import  sys
import  math

t = int(sys.stdin.readline().strip())
inputVal = [int(sys.stdin.readline().strip()) for _ in range(t)]

isPrime = [True] * 10001

def eratosthenes_sieve(n) :
    isPrime[0] = isPrime[1] = False
    
    for x in range(2, math.isqrt(n) + 1) :
        if (isPrime[x] == True) :
            for multiple in range(x * x, n + 1, x) :
                isPrime[multiple] = False

eratosthenes_sieve(10000)

for i in range(t) :
    val1 = val2 = inputVal[i] // 2
    while (True) :
        if (isPrime[val1] and isPrime[val2]) :
            print(f"{val1} {val2}")
            break
        else :
            val1 -= 1
            val2 += 1


