# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return not t
        if not t:
            return False
        return self.isSametree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSametree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)
