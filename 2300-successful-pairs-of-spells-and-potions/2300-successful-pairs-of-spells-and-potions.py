class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # 그냥 풀면 안풀리는 문제.. BINARY SEACRH로 풀어봅니다..
        
        result = []
        potions.sort()
        
        for i in spells:
            tmp = success / i
            result.append(len(potions) - bisect_left(potions, tmp))
        
        return result