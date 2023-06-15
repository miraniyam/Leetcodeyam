# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        result = 10**6 + 1
        
        stack_value = []
        stack = [root]

        while len(stack) > 0:
            item = stack.pop()
            
            if item.left is not None:
                stack.append(item.left)
            if item.right is not None:
                stack.append(item.right)
            
            stack_value.append(item.val)
        
        stack_value.sort()
        
        for i in range(1, len(stack_value)):
            result = min(result, abs(stack_value[i-1]-stack_value[i]))
        
        return result
                