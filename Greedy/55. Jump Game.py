class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_good_index = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last_good_index:
                last_good_index = i

        return last_good_index == 0