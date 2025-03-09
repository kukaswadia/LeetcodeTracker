class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2
            min_split = 1
            current_arr = 0

            for num in nums:
                if current_arr + num > mid:
                    min_split += 1
                    current_arr = num
                else:
                    current_arr += num

            if min_split > k:
                left = mid + 1
            else:
                right = mid
        return left