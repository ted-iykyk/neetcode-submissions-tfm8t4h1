class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupedSum = {}

        for val in strs:
            sumVals = "".join(sorted(val))
            if sumVals not in groupedSum:
                groupedSum[sumVals] = [val]
            else:
                groupedSum[sumVals].append(val)



        return list(groupedSum.values())