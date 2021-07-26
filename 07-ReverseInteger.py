class Solution:
    def reverse(self, x: int) -> int:
        if x > (2**31)-1:
            return
        if x <-2**31:
            return
        if x == 0:
            return 0
        if x >0:
            ans = int(''.join(reversed(str(x))))
        else:
            temp = ''.join(reversed(str(abs(x))))
            ans = int(temp)*-1
        if ans > (2**31)-1:
            return 0
        if ans <-2**31:
            return 0
        return ans
