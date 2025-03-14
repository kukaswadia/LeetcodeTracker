class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        tailLeft, tailRight = left, right

        while head:
            if head.val < x:
                tailLeft.next = head
                tailLeft = tailLeft.next
            else:
                tailRight.next = head
                tailRight = tailRight.next

            head = head.next
        tailLeft.next = right.next
        tailRight.next = None
        return left.next