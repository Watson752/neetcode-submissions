class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = prices[0]
        best = 0

        for p in prices[1:]:
            best = max(best,p-low)
            low = min(low, p)
        return best








