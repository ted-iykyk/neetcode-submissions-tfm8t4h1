class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lenMap = {}
        res = 0
        numSet = set(nums)

        for num in nums:
            if num - 1 in lenMap:
                lenMap[num-1] += 1
            elif num - 1 in numSet:
                tempNum = num - 1
                tempCount = 0
                while tempNum in numSet:
                    tempCount += 1
                    tempNum -= 1
                lenMap[num] = tempCount + 1
            else:
                lenMap[num] = 1

        for val in lenMap.values():
            res = max(val, res)

        return res