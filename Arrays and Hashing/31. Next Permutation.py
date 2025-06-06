class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(ind1, ind2):
            temp = nums[ind1]
            nums[ind1] = nums[ind2]
            nums[ind2] = temp

        def reverse(beg, end):
            while beg < end:
                swap(beg, end)
                beg += 1
                end -= 1

        if len(nums) == 1:
            return

        if len(nums) == 2:
            return swap(0, 1)

        dec = len(nums) - 2
        while dec >= 0 and nums[dec] >= nums[dec + 1]:
            dec -= 1
        reverse(dec + 1, len(nums) - 1)
        if dec == -1:
            return

        next_num = dec + 1

        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
        swap(next_num, dec)