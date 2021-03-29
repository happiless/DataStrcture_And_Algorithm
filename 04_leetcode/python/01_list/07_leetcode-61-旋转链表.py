# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
            旋转链表：1. 计算总链表的长度
                    2. 让链表的尾节点指向头结点
                    3. 因为如果 k > 总长度，则会选择超过一圈, 使 k %= cnt
                    4. 因为要向左移，及向右移动 cnt - k个节点
                    5. 将头结点指向p节点的下一个节点，使p.next = None
        :param head:
        :param k:
        :return:
        """
        if not head: return None
        cnt: int = 1
        p = head
        while p.next:
            p = p.next
            cnt += 1
        p.next = head
        k %= cnt
        k = cnt - k
        while k:
            k -= 1
            p = p.next

        head = p.next
        p.next = None
        return head