class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Two-pointer approach: O(n) time, O(n) space
        """
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        pos = n - 1     # fill the result array from the end 

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            # take the larger square and place at the current position
            if left_square > right_square:
                result[pos] = left_square 
                left += 1

            else:
                result[pos] = right_square
                right -= 1

            pos -= 1

        return result