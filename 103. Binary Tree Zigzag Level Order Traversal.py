# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        out = []
        layer = [root]
        left = 1
        while len(layer) > 0:
            next_layer = []
            values = []
            while len(layer) > 0:
                node = layer.pop(0)
                values.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            if left == -1:
                values.reverse()
            out.append(values)
            layer = next_layer
            left *= -1
        return out