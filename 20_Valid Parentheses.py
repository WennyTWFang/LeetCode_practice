class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1 or len(s)>(10**4)+1:
            return False
        for each_s in s:
            if each_s not in '()[]{}':
                return False
        parentheses_pair = {"(":")", "[":"]", "{":"}"}
        pair_left = 0; True_count = 0; stop = 0
        for j in range(0, len(s)):
            for i in ["()", "{}", "[]"]:
                s = s.replace(i, "")
            if s == "":
                return True
        if len(s)%2 != 0:
            return False
        else:
            for i in range(0, len(s)//2):
                pair_left = -1 * (i+1)
                try:
                    if parentheses_pair[s[i]] == s[pair_left]:
                        True_count += 1
                except:
                    True_count += 0
            if True_count == len(s)//2:
                return True
            else:
                return False
