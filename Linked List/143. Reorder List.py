# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return

            # // split
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        p2 = slow.next
        slow.next = None

        # // reverse
        prev = None
        while p2 and p2.next:
            temp = p2.next
            p2.next = prev
            prev = p2
            p2 = temp
        p2.next = prev

        # // merge
        p1 = head
        while p1 and p2:
            p1next = p1.next
            p2next = p2.next
            p1.next = p2
            p2.next = p1next
            p1 = p1next
            p2 = p2next
