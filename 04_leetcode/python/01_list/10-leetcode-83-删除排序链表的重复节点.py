# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
            1. 通过快慢指针，判断值是否相等，不相等则将慢指针指向快指针，无论是否相等，快指针往后走一步
            2. 如果p的值等于下一个值，则p.next = p.next.next， 不相等则 p = p.next
        :param head:
        :return:
        """
        if not head: return None
        # fast, slow = head, head
        # while fast:
        #     if fast.val != slow.val:
        #         slow.next = fast
        #         slow = slow.next
        #
        #     fast = fast.next
        # slow.next = None
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head