class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return

        mid = end = head
        while end.next and end.next.next:
            end = end.next.next
            mid = mid.next
        p2 = mid.next
        mid.next = None

        prev = None
        while p2 and p2.next:
            p2Next = p2.next
            p2.next = prev
            prev = p2
            p2 = p2Next
        p2.next = prev

        p1 = head
        while p1 and p2:
            p1Next = p1.next
            p2Next = p2.next
            p1.next = p2
            p2.next = p1Next
            p1 = p1Next
            p2 = p2Next