class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0
        n = len(costs)

        left, right = 0, n - 1
        left_heap, right_heap = [], []

        for i in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, (costs[left], left))
                left += 1
            else:
                break

        for i in range(candidates):
            if left <= right:
                heappush(right_heap, (costs[right], right))
                right -= 1
            else:
                break

        for round_num in range(k):
            if left_heap and right_heap:
                if left_heap[0][0] <= right_heap[0][0]:
                    cost, idx = heapq.heappop(left_heap)
                    total_cost += cost
                    if left <= right:
                        heapq.heappush(left_heap, (costs[left], left))
                        left += 1
                else:
                    cost, idx = heapq.heappop(right_heap)
                    total_cost += cost
                    if left <= right:
                        heapq.heappush(right_heap, (costs[right], right))
                        right -= 1

            elif left_heap:
                cost, idx = heapq.heappop(left_heap)
                total_cost += cost
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1

            elif right_heap:
                cost, idx = heapq.heappop(right_heap)
                total_cost += cost
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1

        return total_cost