class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output: List[int] = [1]*len(nums)

        
        for i, v in enumerate(nums):
            curr = 1
            k = 0
            while k < len(nums):
                if k == i:
                    k += 1
                    continue
                curr *= nums[k]
                k += 1
            output[i] = curr



        return output