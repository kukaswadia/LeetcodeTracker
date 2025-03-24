class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        pairs = [(nums2[i], nums1[i]) for i in range(len(nums2))]
        pairs.sort(reverse = True)
        max_score = 0
        current_sum = 0
        heap = []

        for current_nums2, current_nums1 in pairs:
            current_sum += current_nums1
            heapq.heappush(heap, current_nums1)

            if len(heap) > k:
                current_sum -= heapq.heappop(heap)
            if len(heap) == k:
                score = current_sum * current_nums2
                max_score = max(max_score, score)

        return max_score