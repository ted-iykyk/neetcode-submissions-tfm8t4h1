class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not len(nums):
            return 0

        i = 0
        while True:
            if nums[i] == val:
                print(nums[i], i)
                nums.pop(i)
            else:
                i += 1
            
            if i > len(nums) - 1 or not len(nums):
                break 

        return len(nums)