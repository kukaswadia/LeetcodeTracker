# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Iterative Solution
        Time Complexity: O(n) - visit each node once
        Space Complexity: O(1) - only use a few pointers
        """

        dummy = ListNode(0)
        dummy.next = head
        current = dummy 

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next

        """
        Recursive Solution
        Time Complexity: O(n)
        Space Complexity: O(n) - due to recursive stack
        """

        if not head:
            return None

        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
