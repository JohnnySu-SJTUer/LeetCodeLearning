class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit,minPrice = 0,float('inf')
        for price in prices:
            minPrice = min(minPrice,price)
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit

if __name__=='__main__':
    prices = [7,6,4,3,1] #[7,1,5,3,6,4]
    s = Solution
    res = s.maxProfit(s,prices)
    print(res)