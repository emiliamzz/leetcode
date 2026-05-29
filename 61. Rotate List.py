# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head
        if not head.next:
            return head
        l = [head.val]
        copy = head
        while copy.next:
            copy = copy.next
            l.append(copy.val)
        if k % len(l) == 0:
            return head
        k = k % len(l)
        out = l[len(l)-k:]
        out.extend(l[:len(l)-k])
        head = ListNode(val=out[-1])
        for i in range(len(out)-2, -1, -1):
            head = ListNode(val=out[i], next=head)
        return head