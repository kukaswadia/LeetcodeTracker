class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, ch in ((a, 'a'), (b, 'b'), (c, 'c')):
            if count > 0:
                heapq.heappush(max_heap, (-count, ch))

        result = []

        while max_heap:
            cnt1, ch1 = heapq.heappop(max_heap)
            if len(result) >= 2 and result[-1] == result[-2] == ch1:
                if not max_heap:
                    break
                cnt2, ch2 = heapq.heappop(max_heap)
                result.append(ch2)
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(max_heap, (cnt2, ch2))
                heapq.heappush(max_heap, (cnt1, ch1))
            else:
                result.append(ch1)
                cnt1 += 1
                if cnt1 < 0:
                    heapq.heappush(max_heap, (cnt1, ch1))

        return "".join(result)