from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_len = 1
                while curr_num + 1 in nums_set:
                    curr_len += 1
                    curr_num += 1
                max_len = max(max_len, curr_len)

        return max_len
    
sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print(sol.longestConsecutive([1, 2, 0, 1]))  # 3

