class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # Create buckets where index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        # Place each number in its frequency bucket
        # items() method of a Python dictionary returns a list of tuples for each key-value pair in a dictionary
        for num, freq in count.items():
            buckets[freq].append(num)

        # Collect k most frequent elements from highest frequency buckets
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result