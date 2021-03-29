# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return None
        empty = ListNode()
        empty.next = head
        p, q = empty, head
        while n:
            n -= 1;
            q = q.next
        while q:
            p = p.next
            q = q.next
        p.next = p.next.next
        return empty.next