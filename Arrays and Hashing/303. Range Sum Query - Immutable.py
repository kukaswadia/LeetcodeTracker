class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total_sum = 0
        for num in nums:
            total_sum += num
            self.prefix.append(total_sum)
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]