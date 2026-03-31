class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet_s = dict()
        alphabet_t = dict()
        
        for i in range(len(s)):
            if s[i] not in alphabet_s:
                alphabet_s[s[i]] = 1
            else:
                alphabet_s[s[i]] += 1

            if t[i] not in alphabet_t:
                alphabet_t[t[i]] = 1
            else:
                alphabet_t[t[i]] += 1

        return alphabet_s == alphabet_t