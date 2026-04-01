class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = strs[0]

        for i in range(1, len(strs)):
            j = 0
            min_len = min(len(res), len(strs[i]))

            while j < min_len and res[j] == strs[i][j]:
                j += 1

            res = res[:j]

            if res == "":
                return ""

        return res