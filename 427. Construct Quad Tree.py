"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def helper(self, grid):
        node = Node()
        count = 0
        for row in grid:
            count += sum(row)
        if count == 0:
            node.val = False
            node.isLeaf = True
            return node
        if count == len(grid) * len(grid):
            node.val = True
            node.isLeaf = True
            return node

        node.val = True
        node.isLeaf = False

        topLeft = []
        topRight = []
        for row in grid[:int(len(grid) / 2)]:
            topLeft.append(row[:int(len(row) / 2)])
            topRight.append(row[int(len(row) / 2):])
        node.topLeft = self.helper(topLeft)
        node.topRight = self.helper(topRight)

        bottomLeft = []
        bottomRight = []
        for row in grid[int(len(grid) / 2):]:
            bottomLeft.append(row[:int(len(row) / 2)])
            bottomRight.append(row[int(len(row) / 2):])
        node.bottomLeft = self.helper(bottomLeft)
        node.bottomRight = self.helper(bottomRight)

        return node

    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.helper(grid)