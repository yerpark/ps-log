class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num // 2 + 1
        while (start <= end):
            mid = (start + end) // 2
            if (mid * mid == num):
                return True
            elif (mid * mid < num):
                start = mid + 1
            else:
                end = mid - 1
        return False