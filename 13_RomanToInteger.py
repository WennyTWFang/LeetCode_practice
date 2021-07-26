class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s)<1:
            return
        elif len(s)>16:
            return
        ans = 0
        sp_char = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400,"CM":900}
        for x in sp_char:
            if x in s:
                ans += sp_char[x]
                s = s.replace(x, "")
        sep_s = list(s)
        characters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in sep_s:
            if i not in characters:
                return
        #while ans>4000 or counter < 0:
        for counter in range(0, len(s)):
            ans += characters[sep_s[counter]]
        if ans>4000:
            return
        return ans