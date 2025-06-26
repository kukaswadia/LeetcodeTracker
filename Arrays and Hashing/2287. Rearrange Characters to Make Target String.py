class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_counts = Counter(s)
        target_counts = Counter(target)
        total_words = float('inf')
        for char in target_counts:
            total_words = min(total_words, s_counts[char] // target_counts[char])
        return total_words