class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)!= 1 and a[0] == 0:
            return False
        elif len(b)!= 1 and b[0] == 0:
            return False
        for i in a:
            if i not in ["1", "0"]:
                return False
        for i in b:
            if i not in ["1", "0"]:
                return False
        if len(a)<1 or len(b)<1 or len(a)>(10**4)+1 or len(b)>(10**4)+1:
            return False
        ans = 0
        new_a = int(a, 2)
        new_b = int(b, 2)
        ans = new_a + new_b
        return format(ans,"b")
