# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        vals = [list1.val, list2.val]
        while list1.next:
            list1 = list1.next
            vals.append(list1.val)
        while list2.next:
            list2 = list2.next
            vals.append(list2.val)
        vals.sort()
        node = ListNode(val=vals[-1])
        vals.pop()
        while len(vals) > 0:
            node = ListNode(val=vals[-1], next=node)
            vals.pop()
        return node