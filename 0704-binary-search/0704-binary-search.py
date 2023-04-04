import heapq

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        heapq.heapify(nums)
        
        count = 0
        while(len(nums) > 0):
            temp = heapq.heappop(nums)
            if temp == target:
                return count
            else:
                count += 1
        
        return -1
        