class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        memo = []
        for i in range(0, rowIndex+1):
            memo.append([1 for _ in range(0, i+1)])
        
        for i in range(1, len(memo)):
            for j in range(1, len(memo[i])-1):
                memo[i][j] = memo[i-1][j-1]+memo[i-1][j]
        
        return memo[rowIndex]