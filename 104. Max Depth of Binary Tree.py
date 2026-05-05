# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, depth):
        if not root.left and not root.right:
            return depth
        new_depth = depth + 1
        if not root.left:
            return self.helper(root.right, new_depth)
        if not root.right:
            return self.helper(root.left, new_depth)
        right = self.helper(root.right, new_depth)
        left = self.helper(root.left, new_depth)
        return max(right, left)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.helper(root, 1)