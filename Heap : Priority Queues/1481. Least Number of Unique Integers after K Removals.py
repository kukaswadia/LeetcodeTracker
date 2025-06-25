class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        heap = list(freq.values())
        heapq.heapify(heap)

        while k > 0 and heap:
            smallest = heapq.heappop(heap)
            if k >= smallest:
                k -= smallest
            else:
                heapq.heappush(heap, smallest)
                break

        return len(heap)