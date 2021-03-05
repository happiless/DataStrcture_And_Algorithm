# 判断链表是否成环
# 解决思路： 利用快慢指针判断链表是否成环，p为慢指针， q为快指针

class Solution:
	def hasCycle(head: ListNode) -> bool:
		if head is None: return False
		p, q = head, head.next
		while p != q and q and q.next:
			p = p.next
			q = q.next
		return q and q.next

