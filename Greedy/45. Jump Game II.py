class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0     # end range of the current jump
        farthest = 0        # fathest position we can reach

        # we don't need to jump from the last position
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # we increase the jumps once we have explored all the possible jumps within our current jump's range
            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= len(nums) - 1:
                    break
        return jumps