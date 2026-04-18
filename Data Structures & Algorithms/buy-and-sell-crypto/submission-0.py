class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        maxprofit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                currprofit = prices[r]-prices[l]
                maxprofit = max(currprofit,maxprofit)
            else:
                l = r
            r +=1
                
        return maxprofit 

        