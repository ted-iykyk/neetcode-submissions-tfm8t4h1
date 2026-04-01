class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        nums.sort()
        # [val, occurance]
        res = [nums[0], 1]
        curr = [nums[0], 1]
        print(nums)
        for i in range(1, len(nums)):
            print(nums[i], curr)
            if nums[i] != curr[0]:
                if res[1] < curr[1]:
                    res = curr
                curr = [nums[i], 1]
            else:
                curr[1] += 1

        if res[1] < curr[1]:
            res = curr

        return res[0]