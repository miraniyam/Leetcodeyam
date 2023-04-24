class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort(reverse=True)
        
        while True:
            if len(stones) <= 1:
                break
            else:
                y = stones[0]
                x = stones[1]
                
                stones = stones[2:]
                
                if x != y :
                    stones.append(y-x)
                stones.sort(reverse=True)
                
        
        return stones[0] if len(stones) > 0 else 0
        