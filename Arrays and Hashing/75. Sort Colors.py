class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = len(nums) - 1

        while white <= blue:
            curr = nums[white]
            if curr == 0:
                nums[white] = nums[red]
                nums[red] = 0
                red += 1
                white += 1

            if curr == 1:
                white += 1

            if curr == 2:
                nums[white] = nums[blue]
                nums[blue] = 2
                blue -= 1