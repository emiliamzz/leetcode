# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, preorder: List[int], inorder: List[int], tree: TreeNode) -> TreeNode:
        if len(preorder) == 1:
            return tree
        i = inorder.index(tree.val)
        if i == 0:
            tree.right = self.recurse(preorder[1:], inorder[1:], TreeNode(val=preorder[1]))
        elif i == len(inorder) - 1:
            preorder.remove(tree.val)
            inorder.pop(-1)
            tree.left = self.recurse(preorder, inorder, TreeNode(val=preorder[0]))
        else:
            il = inorder[:i]
            ir = inorder[i+1:]
            pl = []
            pr = []
            for node in preorder:
                if node in il:
                    pl.append(node)
                if node in ir:
                    pr.append(node)
            tree.left = self.recurse(pl, il, TreeNode(val=pl[0]))
            tree.right = self.recurse(pr, ir, TreeNode(val=pr[0]))
        return tree

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.recurse(preorder, inorder, TreeNode(val=preorder[0]))