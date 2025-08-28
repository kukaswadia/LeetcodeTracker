class Solution:
    def reverse(self, x: int) -> int:
        # Handle the sign of the integer
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the digits
        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10

        # Restore the sign
        reversed_x *= sign

        # Check for 32-bit signed integer overflow
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0

        return reversed_x