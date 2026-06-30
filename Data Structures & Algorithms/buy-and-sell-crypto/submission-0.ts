class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        let profit = 0
        let right = 0

        prices.forEach((price: number, i: number) => {
            right = i + 1
            while (right < prices.length) {
                let temp = prices[right] - price
                if (temp > profit) {
                    profit = temp
                }
                right++
            }
        })


        return profit
    }
}
