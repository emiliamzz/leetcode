# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search(self, root, v):
        if root == v:
            return True
        if root.left:
            if self.search(root.left, v):
                return True
        if root.right:
            if self.search(root.right, v):
                return True
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root == p or root == q:
                return root
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                p_left = self.search(root.left, p)
                q_left = self.search(root.left, q)
                if p_left and q_left:
                    root = root.left
                if not p_left and not q_left:
                    root = root.right
                else:
                    return root
