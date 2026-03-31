class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            for char in s:
                res+=char
            res+="'"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        tmp = ""
        for char in s:
            if char != "'":
                tmp+=char
            else:
                res.append(tmp)
                tmp=""

        return res