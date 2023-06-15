# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sumOfnodes = dict()
        
        def dfs(sumOfnodes, node, level):
            if level in sumOfnodes.keys():
                sumOfnodes[level] += node.val
            else:
                sumOfnodes[level] = node.val
            
            if node.left is not None:
                dfs(sumOfnodes, node.left, level+1)
            if node.right is not None:
                dfs(sumOfnodes, node.right, level+1)
            
            return sumOfnodes
    
        sumOfnodes = dfs(sumOfnodes, root, 1)
        maxValue = max(sumOfnodes.values())
        
        return [i for i in sumOfnodes.keys() if sumOfnodes[i] == maxValue][0]