# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, num):
        if not root.left and not root.right:
            return num * 10 + root.val
        if not root.left:
            return self.helper(root.right, num * 10 + root.val)
        if not root.right:
            return self.helper(root.left, num * 10 + root.val)
        return self.helper(root.left, num * 10 + root.val) + self.helper(root.right, num * 10 + root.val)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.helper(root, 0)