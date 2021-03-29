# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        empty = ListNode()
        empty.next = head
        p = empty
        while p.next:
            if p.next.next and p.next.val == p.next.next.val:
                q = p.next.next
                while q and q.val == p.next.val:
                    q = q.next
                p.next = q

            else:
                p = p.next
        return empty.next
