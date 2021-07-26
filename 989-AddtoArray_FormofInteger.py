class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        new_num = ""
        for i in num:
            new_num = "{}{}".format(new_num, i)
        num = int(new_num)
        ans = num + k
        return list(str(ans))
