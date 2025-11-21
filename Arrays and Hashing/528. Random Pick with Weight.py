class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        running_sum = 0

        for weight in w:
            running_sum += weight
            self.prefix_sums.append(running_sum)

        self.total_sum = running_sum
        

    def pickIndex(self) -> int:
        target = randint(1, self.total_sum)

        left, right = 0, len(self.prefix_sums) - 1

        while left < right: 
            mid = left + (right - left) // 2

            if self.prefix_sums[mid]< target:
                left = mid + 1
            else: 
                right = mid 
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
