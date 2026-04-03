class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, lp, rp, m):
            i, j, k = lp, 0, 0

            leftArr = arr[lp:m+1]
            rightArr = arr[m+1:rp+1]

            while j < len(leftArr) and k < len(rightArr):
                if leftArr[j] <= rightArr[k]:
                    arr[i] = leftArr[j]
                    j += 1
                else:
                    arr[i] = rightArr[k]
                    k += 1
                
                i += 1
            
            while j < len(leftArr):
                arr[i] = leftArr[j]
                j += 1
                i += 1
            
            while k < len(rightArr):
                arr[i] = rightArr[k]
                k += 1
                i += 1
            
            return arr

        def mergeSort(arr, lp, rp):
            if lp == rp:
                return arr
            
            m = (lp + rp) // 2

            mergeSort(arr, lp, m)
            mergeSort(arr, m+1, rp)
            merge(arr, lp, rp, m)

            return arr

        return mergeSort(nums, 0, len(nums) - 1)

