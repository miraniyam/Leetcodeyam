import heapq

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self._nums = nums
        self._k = k

    def add(self, val: int) -> int:
        self._nums.append(val)
        self._nums.sort(reverse = True)
        return self._nums[self._k-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)