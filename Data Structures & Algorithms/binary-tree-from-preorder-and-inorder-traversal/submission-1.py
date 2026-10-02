# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        i = 0
        graph = defaultdict(int) # value --> preorder idx
        for j in range(len(inorder)):
            graph[inorder[j]] = j
        def dfs(l, r):
            nonlocal i
            if l > r:
                return None
            root = TreeNode(preorder[i])
            idx = graph[preorder[i]]
            i += 1
            root.left = dfs(l, idx - 1)
            root.right = dfs(idx + 1, r)
            return root
        
        return dfs(0, len(preorder) - 1)