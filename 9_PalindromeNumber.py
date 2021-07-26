class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >(2**31)-1 or x<-2**31:
            return
        elif x<0:
            return False
        y = ""
        for i in range(len(str(x))-1, -1, -1):
            y = y + str(x)[i]
        if y == str(x):
            return True
        else:
            return False