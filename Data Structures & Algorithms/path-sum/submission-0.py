# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if targetSum == 0:
            return True
        if not root:
            return False
        if self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val):
            return True
        return False