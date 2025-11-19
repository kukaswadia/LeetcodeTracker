class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        ones = 0

        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
            
            # We will enter the elif block if the current character is 0
            elif i > 0 and s[i - 1] == '1':
                result += ones

        return result
        
