class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            tmp = []
            cycle = 0

            for i in range(n + 1):
                if max_heap:
                    count = heapq.heappop(max_heap)
                    cycle += 1
                    if count + 1 < 0:
                        tmp.append(count + 1)
                else:
                    cycle += 1

                time += 1
                if not max_heap and not tmp:
                    break

            for item in tmp:
                heapq.heappush(max_heap, item)

        return time