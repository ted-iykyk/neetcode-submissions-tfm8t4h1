class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        end = len(numbers) - 1
        
        st = 0

        while numbers[end] + numbers[st] != target:
            if numbers[end] + numbers[st] > target:
                end -= 1
            else:
                st += 1


        return [st+1, end+1]