class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<1 or len(strs)>200:
            return
        elif len(strs) ==1:
            return strs[0]
        newstrs = [];lower_strs=[]
        for each_str in strs:
            if len(each_str)>200:
                return
            elif len(each_str)==0:
                return ""
            each_str = each_str.lower()
            lower_strs.append(each_str)
        list_len = list(map(len, lower_strs))
        min_len = min(list_len)
        position = list_len.index(min_len)
        for i in lower_strs:
            newstrs.append(i[0:min_len])
        temp = newstrs[0][0]
        prefix = ""
        for i in range(0, min_len):
            coti = 0
            for j in newstrs:
                if temp == j[0:i+1]:
                    coti += 1
            if coti == len(newstrs):
                prefix = temp
            else:
                break
            temp = newstrs[0][0:i+2]
        for i in newstrs:
            if prefix not in i :
                return ""
        return prefix 
