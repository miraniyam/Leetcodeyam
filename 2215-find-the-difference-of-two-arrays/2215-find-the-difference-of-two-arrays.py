class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result1 = set(nums1) - set(nums2)
        result2 = set(nums2) - set(nums1)
        
        return [result1, result2]