# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, left, right):
        if left.val != right.val:
            return False
        if left.left and not right.right:
            return False
        if left.right and not right.left:
            return False
        if right.left and not left.right:
            return False
        if right.right and not left.left:
            return False
        if not left.left and not left.right and not right.left and not right.right:
            return True
        if left.left:
            if not self.recurse(left.left, right.right):
                return False
        if left.right:
            if not self.recurse(left.right, right.left):
                return False
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left and not root.right:
            return False
        if root.right and not root.left:
            return False
        if not root.left and not root.right:
            return True
        return self.recurse(root.left, root.right)