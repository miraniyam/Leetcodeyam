class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        
        dt = {} # key = (day, isStock), value = profit
        
        def maxProfitForDay(day, isStock):
            if day == len(prices):
                # last day, can't do anything
                return 0
            
            if (day, isStock) in dt:
                return dt[(day, isStock)]
            
            if isStock == False:
                # buy or do-nothing
                dt[(day, isStock)] = max(maxProfitForDay(day+1, True) - prices[day], maxProfitForDay(day+1, False))
            else:
                # sell or do-nothing
                dt[(day, isStock)] = max(maxProfitForDay(day+1, False) + prices[day], maxProfitForDay(day+1, True))
            
            return dt[(day, isStock)]
            
        
        return maxProfitForDay(0, False)