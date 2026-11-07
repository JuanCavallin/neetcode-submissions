# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, largest):
            if not root:
                return 0

            left, right = dfs(root.left, max(largest, root.val)), dfs(root.right, max(largest, root.val))
            result = left + right
            if root.val >= largest:
                result += 1
            return result
        
        return dfs(root, root.val)
        
        