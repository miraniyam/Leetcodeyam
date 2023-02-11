class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            # remove i-th element in nums
            temp = nums[:i] + nums[i+1:]
            subtemp = [0] + temp[:len(temp)-1]
            result = [x - y for x, y in zip(temp, subtemp)]
            if min(result) > 0:
                return True
        return False