class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1) - constant space
        """
        slow = n 
        fast = n

        while True:
            slow = self.get_sum_of_squares(slow)
            fast = self.get_sum_of_squares(self.get_sum_of_squares(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False

    def get_sum_of_squares(self, n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit 
            n //= 10
        return total