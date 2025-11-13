# 모듈러 연산의 개념을 물어보는 느낌 ..?! 
# 모듈러 연산 - 나머지 구하는 연산
# 빠른 거듭제곱 - aka 거듭제곱 분할 정복 

import sys, math

def get_mod_pow(base, exponent, mod):
    if exponent <= 1:
        return base % mod
    
    if exponent % 2 == 0:
        half = get_mod_pow(base, exponent // 2, mod) % mod
        return (half * half) % mod
    else:
        half = get_mod_pow(base, exponent - 1, mod)
        return (base * (half % mod)) % mod

if __name__ == "__main__":
    a, b, c = map(int, sys.stdin.readline().split())

    print(get_mod_pow(a, b, c))