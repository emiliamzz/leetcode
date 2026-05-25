# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, p, q):
        if p.val != q.val:
            return False
        if p.left and not q.left:
            return False
        if q.left and not p.left:
            return False
        if p.right and not q.right:
            return False
        if q.right and not p.right:
            return False
        if p.left:
            is_same = self.recurse(p.left, q.left)
            if not is_same:
                return False
        if p.right:
            is_same = self.recurse(p.right, q.right)
            if not is_same:
                return False
        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return self.recurse(p, q)