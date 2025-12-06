"""
Why use a set? 
- Converting jewels to a set optimizes search operations from O(n) linear search to O(1) constant-time lookups. 
- Without a set, you would need nested loops O(n x m) time complexity. 

"Time: O(J + S) where J is the length of jewels and S is the length of stones. 
Space: (J) for storing the jewel set"
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        count = 0

        for s in stones:
            if s in jewels:
                count += 1
        return count
