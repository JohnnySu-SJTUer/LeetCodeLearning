class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if not len(prices):
        #     return 0
        # prices.append(0)
        # minPrice = float('inf')
        # lastPrice = prices[0]
        # sumProfit = 0
        # for  price in prices:
        #     if lastPrice>price:
        #         minPrice = price
        #         sumProfit += lastProfit
        #     minPrice = min(minPrice,price)
        #     profit = price - minPrice
        #     lastProfit = profit
        #     lastPrice = price
        # return sumProfit

        if not len(prices):
            return 0
        sumProfit = 0
        for i in range(len(prices)-1):
            if 0 < prices[i+1]-prices[i]:
                sumProfit += prices[i+1]-prices[i]
        return sumProfit

if __name__=='__main__':
    prices = [1,2,3,4,5] #[7,1,5,3,6,4]
    s = Solution
    res = s.maxProfit(s,prices)
    print(res)