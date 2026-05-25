# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, arr, branch):
        arr.append(branch.val)
        if branch.left == None and branch.right == None:
            return arr
        if branch.right == None:
            return self.rec(arr, branch.left)
        if branch.left == None:
            return self.rec(arr, branch.right)
        return self.rec(arr, branch.left) + self.rec(arr, branch.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = list(set(self.rec([], root)))
        arr.sort()
        if len(arr) == 2:
            return arr[1] - arr[0]
        min_diff = arr[1] - arr[0]
        if min_diff == 1:
            return 1
        for i in range(1, len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff == 1:
                return 1
            if diff < min_diff:
                min_diff = diff
        return min_diff