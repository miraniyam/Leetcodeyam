class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        minVal = 10**4 + 1
        
        for i in range(len(prices)):
            answer = max(answer, prices[i] - minVal)
            minVal = min(prices[i], minVal)
        
        return answer