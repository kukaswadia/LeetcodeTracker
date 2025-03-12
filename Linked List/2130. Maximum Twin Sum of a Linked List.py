class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev
        max_sum = 0
        while head2:
            max_sum = max(max_sum, head.val + head2.val)
            head = head.next
            head2 = head2.next
        return max_sum