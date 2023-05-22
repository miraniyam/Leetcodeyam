from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        return list(map(lambda x: x[0], Counter(nums).most_common(k)))
            