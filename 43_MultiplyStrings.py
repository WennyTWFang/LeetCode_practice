class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        try:
            num1 = int(num1)
            num2 = int(num2)
        except:
            return
        ans = num1*num2
        return str(ans)
