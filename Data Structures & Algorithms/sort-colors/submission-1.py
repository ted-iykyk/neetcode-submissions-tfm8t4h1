class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        bucket = [0]*3

        for num in nums:
            if num == 0:
                bucket[0] += 1
            elif num == 1:
                bucket[1] += 1
            else:
                bucket[2] += 1
        
        i = 0
        j = 0
        print(bucket)
        while j <= 2 and i < len(nums):
            if bucket[j] == 0:
                j += 1
            else:
                nums[i] = j
                bucket[j] -= 1
                i += 1
        
        return nums
        


        
       