import sys

testCase = int(sys.stdin.readline().strip())

for _ in range(testCase) :
    repeatVal, str = sys.stdin.readline().split()
    repeatVal = int(repeatVal)
    newStr = "".join([x * repeatVal for x in str])
    print(newStr)