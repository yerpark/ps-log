import sys
buffer = []
bufferFlag = 0

n = int(sys.stdin.readline().strip())

if (n <= 20) :
    bufferFlag = 1

def recursive_hanoi(num, start, mid, end) :
    if (num == 1) :
        if bufferFlag == 1 :
            buffer.append(f"{start} {end}")
        return (1)
    else :
        if bufferFlag == 1 :
            res = recursive_hanoi(num - 1, start, end, mid)
            buffer.append(f"{start} {end}")
            res += 1 + recursive_hanoi(num - 1, mid, start, end)
            return (res)
        else :
            return (1 + 2 * (recursive_hanoi(num - 1, start, mid, end)))
    
print (recursive_hanoi(n, 1, 2, 3))
if bufferFlag == 1 :
    print("\n".join(buffer))