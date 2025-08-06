class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        
        while r < len(prices):
            
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            r += 1

        return res

# Time comp: O(n) since only iterate through list once
# Space comp: O(1) since only storing two pointers --- l and r
