class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def helper(left, right):
            cnt = 0
            while left >= 0 and right < n and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt

        for i in range(n):
            count += helper(i, i)
            count += helper(i, i + 1)

        return count