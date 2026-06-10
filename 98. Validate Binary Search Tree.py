# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: TreeNode, a: int=None, b: int=None) -> bool:
        if root.left:
            if root.left.val >= root.val:
                return False
            if a and root.left.val <= a:
                return False
            if b and root.left.val >= b:
                return False
            if a and b:
                if not self.helper(root.left, a, min(root.val, b)):
                    return False
            elif a:
                if not self.helper(root.left, a, root.val):
                    return False
            elif b:
                if not self.helper(root.left, None, min(root.val, b)):
                    return False
            else:
                if not self.helper(root.left, None, root.val):
                    return False
        if root.right:
            if root.right.val <= root.val:
                return False
            if a and root.right.val <= a:
                return False
            if b and root.right.val >= b:
                return False
            if a and b:
                if not self.helper(root.right, max(root.val, a), b):
                    return False
            elif a:
                if not self.helper(root.right, max(root.val, a), None):
                    return False
            elif b:
                if not self.helper(root.right, root.val, b):
                    return False
            else:
                if not self.helper(root.right, root.val, None):
                    return False
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.right or root.left:
            return self.helper(root, None, None)
        return True