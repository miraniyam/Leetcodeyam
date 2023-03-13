# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftStack = []
        rightStack = []
        
        self.searchLeft(root.left, leftStack)
        self.searchRight(root.right, rightStack)
        
        for i in range(0, len(leftStack)):
            if leftStack[i] != rightStack[i]:
                return False
        return True
            
    
    def searchLeft(self, node, stack):
        if node is None:
            stack.append(None)
        else:
            stack.append(node.val)
            self.searchLeft(node.left, stack)
            self.searchLeft(node.right, stack)
    
    def searchRight(self, node, stack):
        if node is None:
            stack.append(None)
        else:
            stack.append(node.val)
            self.searchRight(node.right, stack)
            self.searchRight(node.left, stack)