class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)

        # creating prefix arr
        for i, v in enumerate(nums):
            if i == 0:
                continue
            output[i] = output[i-1] * nums[i-1]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            
            if i == len(nums) - 1:
                continue
            post *= nums[i+1]
            output[i] = output[i] * post


        return output

