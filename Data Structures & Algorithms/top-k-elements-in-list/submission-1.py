class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        res = [0] * k
        freq_dict = defaultdict(int)

        for num in nums:
            freq_dict[num] += 1
        
        i = 0
        while i < k:
            max_val = 0
            for key, value in freq_dict.items():
                if value > max_val:
                    max_val = value
                    max_val_key = key

            res[i] = max_val_key
            freq_dict[max_val_key] = 0
            i += 1



        return res