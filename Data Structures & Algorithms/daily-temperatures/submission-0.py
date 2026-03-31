class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            curr = i
            while curr <= len(temperatures) - 1:
                if v < temperatures[curr]:
                    res[i] = curr- i
                    break
                curr += 1
        

        return res