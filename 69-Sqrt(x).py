class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0 or x>(2**31):
            return False
        ans = 0
        for i in range(0, x+1):
            if i**2<=x:
                ans = i
            else:
                break
        return ans
