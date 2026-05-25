"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def recurse(self, head: Node, nodes: List[Node], nodes_copy: List[Node]) -> Node:
        node = Node(head.val)
        nodes.append(head)
        nodes_copy.append(node)
        if head.next:
            node.next = self.recurse(head.next, nodes, nodes_copy)
        if head.random:
            node.random = nodes_copy[nodes.index(head.random)]
        return node

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        return self.recurse(head, [], [])