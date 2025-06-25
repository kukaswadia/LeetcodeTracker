class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        n = len(s)

        if max(counter.values()) > (n + 1) // 2:
            return ""

        max_heap = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(max_heap)
        result = []

        while len(max_heap) >= 2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)

            result.append(char1)
            result.append(char2)

            if -freq1 > 1:
                heapq.heappush(max_heap, (freq1 + 1, char1))
            if -freq2 > 1:
                heapq.heappush(max_heap, (freq2 + 1, char2))

        if max_heap:
            result.append(max_heap[0][1])

        return ''.join(result)