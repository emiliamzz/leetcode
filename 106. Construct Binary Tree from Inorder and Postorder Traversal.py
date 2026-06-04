# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 1:
            return TreeNode(val=inorder[0])
        root = TreeNode(val=postorder[-1])
        index = inorder.index(postorder[-1])
        inorderLeft = inorder[:index]
        inorderRight = inorder[index+1:]
        postorderRight = []
        postorderLeft = []
        for value in postorder[:-1]:
            if value in inorderRight:
                postorderRight.append(value)
            else:
                postorderLeft.append(value)
        if len(inorderRight) > 0:
            root.right = self.buildTree(inorderRight, postorderRight)
        if len(inorderLeft) > 0:
            root.left = self.buildTree(inorderLeft, postorderLeft)
        return root