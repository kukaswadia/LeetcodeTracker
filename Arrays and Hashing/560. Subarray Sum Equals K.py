class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1

        for num in nums:
            prefix_sum += num
            num_required= prefix_sum - k
            if num_required in sum_freq:
                count += sum_freq[num_required]
            sum_freq[prefix_sum] += 1

        return count