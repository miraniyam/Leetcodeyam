class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
                
        memo = [[100*200*200+1] * n for i in range(m)]
        
        memo[0][0] = grid[0][0]
    
        for i in range(m):
            for j in range(n):
                right = 100*200*200+1
                down = 100*200*200+1
                
                if j-1 >= 0: right = memo[i][j-1]
                
                if i-1 >= 0: down = memo[i-1][j]
                
                memo[i][j] = min(memo[i][j], grid[i][j] + right, grid[i][j] + down)
                
    
        return memo[m-1][n-1]
        