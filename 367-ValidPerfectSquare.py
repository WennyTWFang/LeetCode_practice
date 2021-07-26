class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0 or num>(2**31):
            return False
        ans = 0
        for i in range(0, num+1):
            if i**2<=num:
                ans = i
            else:
                break
        if ans **2 == num:
            return True
        else: False
