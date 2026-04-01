class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        res = strs[0]

        for i in range(1,len(strs)):
            if strs[i] == "":
                return ""
            temp = ""
            k = 0
            p = 0
            minLen = min(len(strs[i]), len(strs[i-1]))
            kWord = strs[i-1]
            pWord = strs[i]

            while k < minLen and kWord[k] == pWord[p]:
                if kWord[k] == pWord[p]:
                    temp += kWord[k]
                k += 1
                p += 1
            if k == 0:
                return ""
            if len(res) >= len(temp):
                res = temp
                                        
        
        return res