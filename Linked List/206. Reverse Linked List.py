# ---------------------------Iterative---------------------------
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

# ---------------------------Recursive---------------------------

class Solution:
    def helper(self, prev, curr):
        if curr is None:
            return prev

        next_node = curr.next
        curr.next = prev
        new_head = self.helper(curr, next_node)
        return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(None, head)