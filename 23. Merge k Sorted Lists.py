# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = ListNode(val=lists[0].val)
        if len(lists) == 1:
            if lists[0].next == None:
                return node
            node.next = self.helper(lists=[lists[0].next])
            return node
        if lists[0].next == None:
            node.next = self.helper(lists=lists[1:])
            return node
        lists[0] = lists[0].next
        i = 1
        while i < len(lists) and lists[i-1].val > lists[i].val:
            copy = lists[i-1]
            lists[i-1] = lists[i]
            lists[i] = copy
            i += 1
        node.next = self.helper(lists=lists)
        return node

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Remove all Nones
        indexes = []
        for i in range(len(lists)):
            if lists[i] == None:
                indexes.append(i)
        for i in range(len(indexes)-1, -1, -1):
            lists.pop(indexes[i])
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return self.helper(lists=lists)
        # Sort the lists
        unsorted = True
        while unsorted:
            unsorted = False
            for i in range(len(lists)-1):
                if lists[i].val > lists[i+1].val:
                    copy = lists[i]
                    lists[i] = lists[i+1]
                    lists[i+1] = copy
                    unsorted = True
        return self.helper(lists=lists)