# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, node: TreeNode, toAttach: Optional[TreeNode]):
        if not node.left and not node.right:
            if toAttach:
                node.right = self.recurse(toAttach, None)
            return node
        if not node.left:
            node.right = self.recurse(node.right, toAttach)
            return node
        if not node.right:
            node.right = self.recurse(node.left, toAttach)
            node.left = None
            return node
        node.right = self.recurse(node.left, node.right)
        node.left = None
        if toAttach:
            node.right = self.recurse(node.right, toAttach)
        return node

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            root = self.recurse(root, None)