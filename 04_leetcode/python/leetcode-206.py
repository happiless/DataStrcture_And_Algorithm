# 解题思路：1. 引入虚拟头 pre， 当前节点cur， 当前的下一个节点 p
#         2. 只要当前 cur节点不为空就循环，
#            1）将当前的下一个节点指向pre，
#            2）并将cur赋值给pre
#            3）将p赋值给cur
#            4）如果p不为空，就将p赋值为p的下一个节点

# 递归方式：1. 先递归到最深的
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        pre = None
        cur = head
        p = head.next
        while cur:
            cur.next = pre
            pre = cur
            cur = p
            if p:
                p = p.next
        return pre

    def reverseListByRecision(self, head:ListNode) -> ListNode:
        if not head and not head.next: return head
        tail = head.next
        p = self.reverseListByRecision(tail)
        head.next = tail.next
        tail.next = head
        return p