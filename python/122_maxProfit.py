# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/22/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

## solution-1
        buyin = False
        price = 0
        profit = 0
        i = 0
        for i in range(len(prices)-1):
            if not buyin:
                if prices[i] < prices[i+1]:
                    buyin = True
                    price = prices[i]
                else:
                    continue
            
            if buyin:
                if prices[i] > prices[i+1]:
                    buyin = False
                    profit += (prices[i]-price)
                else:
                    if i+1 == len(prices)-1:
                        profit += (prices[i+1]-price)
                    else:
                        continue
        return profit

## solution-2
        profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
        return profit