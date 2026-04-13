class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        # creating prefix arr
        for i, v in enumerate(nums):
            if i == 0:
                continue
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            postfix[i] = postfix[i+1] * nums[i+1]


        output = []

        for i in range(len(nums)):
            output.append(postfix[i] * prefix[i])

        return output

