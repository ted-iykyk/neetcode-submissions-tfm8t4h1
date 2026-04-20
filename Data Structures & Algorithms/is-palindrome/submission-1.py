class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = ""

        for val in s:
            if val.isalnum():
                clean += val.lower()
        
        st = 0
        e = len(clean) - 1

        while st < e:
            if clean[st] != clean[e]:
                return False

            st += 1
            e -= 1



        return True