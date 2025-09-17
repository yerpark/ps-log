import sys

year = (int)(sys.stdin.readline().strip())
yearType = 0

if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))) :
    yearType = 1

print (yearType)
