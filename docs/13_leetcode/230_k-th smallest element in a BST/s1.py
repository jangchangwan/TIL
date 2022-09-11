# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 100 ms	18.2 MB
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k):
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        ans = inorder(root)
        return ans[k - 1]