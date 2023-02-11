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

"""
class Solution(object):
    def canBeIncreasing(self, nums):
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                print("  count")
                count += 1
                if i>1 and nums[i] <= nums[i-2]:
                    print("  milgy")
                    nums[i] = nums[i-1]
            print(f"[{i}] {nums[i]} {nums}")
        return count <= 1
"""