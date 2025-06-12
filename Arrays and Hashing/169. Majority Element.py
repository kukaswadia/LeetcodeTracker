class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        counts = 0
        for num in nums:
            if counts == 0:
                element = num

            if element == num:
                counts += 1
            else:
                counts -= 1

        return element