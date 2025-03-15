class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy

        while True:
            kth = pre
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next

            prev = group_next
            curr = pre.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = pre.next
            pre.next = kth
            pre = temp
        return dummy.next