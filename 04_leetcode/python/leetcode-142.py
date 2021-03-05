# 环形链表
# 解题思路：1. 通过快慢指针判断链表是否成环；q 为慢指针， p为快指针
#			2. 当慢指针走到环入口的距离为 a， 快指针走的距离则为 2a，
#			3. 假设快指针走到环入口的距离为 x，则环的长度为 a+x，
#			4. 因为快指针每次走两步，慢指针每次走一步，所以再走 x 步，快指针会追上慢指针
#			5. 此时慢指针走了 x 步，离环入口还差 a+x-x=a 步

class Solution:
	def deleteCycle(self, head: ListNode) -> ListNode:
		if head is None or head.next: return None
		p, q = head.next, head.next.next
		while p != q and q and q.next:
			p = p.next
			q = q.next.next
		if q is None or q.next is None: return None
		p = head
		while p != q:
			p = p.next
			q = q.next
		return q

