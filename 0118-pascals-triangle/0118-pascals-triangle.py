"""
k row
node[i] = node[k]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo = []
        for i in range(numRows):
            memo.append([1 for _ in range(0,i+1)])
        
        for i in range(1, len(memo)):
            for j in range(1, len(memo[i])-1):
                # if i == 0 or j == 0:
                #     continue
                # if j > len(memo[i-1]) - 1:
                #     continue
                memo[i][j] = memo[i-1][j-1]+memo[i-1][j]
                
        return memo
                
        
        