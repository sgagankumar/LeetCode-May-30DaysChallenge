class Solution:
	def oddEvenList(self, head: ListNode) -> ListNode:
		if not head or not head.next or not head.next.next:
			return head
		odd=ListNode(next=None)
		even=ListNode(next=None)
		tempodd=odd
		tempeven=even
		flag=True
		while head:
			if flag:
				odd.next=head
				head=head.next
				odd=odd.next
				flag=False
			else:
				even.next=head
				head=head.next
				even=even.next
				flag=True
		even.next=None
		odd.next=tempeven.next
		
		return tempodd.next