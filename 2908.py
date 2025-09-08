import sys

inputVal = sys.stdin.readline().split()

reverseVal1 = inputVal[0][::-1]
reverseVal2 = inputVal[1][::-1]

print(max(int(reverseVal1), int(reverseVal2)))