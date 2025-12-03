class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Time: O(m + n) where m = len(ransomNote), n = len(magazine)
        Space: O(1) - at most 26 lowercase letters
        """
        magazine_count = Counter(magazine)
        for char in ransomNote:
            if magazine_count[char] <= 0:
                return False
            magazine_count[char] -= 1 
        return True
        