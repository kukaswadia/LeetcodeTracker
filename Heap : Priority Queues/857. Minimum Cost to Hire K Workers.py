class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        workers = [(wage[i] / quality[i], quality[i]) for i in range(n)]
        workers.sort(key = lambda x : x[0])

        heap = []
        quality_sum = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(heap, -q)
            quality_sum += q

            if len(heap) > k:
                removed_quality = -heapq.heappop(heap)
                quality_sum -= removed_quality

            if len(heap) == k:
                cost = quality_sum * ratio
                min_cost = min(min_cost, cost)

        return min_cost