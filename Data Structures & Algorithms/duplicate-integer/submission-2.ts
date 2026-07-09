class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {

        const dups = new Set<number>();

        for (const num of nums){
            if (!(dups.has(num))){
                dups.add(num)
            }
            else return true
        }

        return false
    }
}
