class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted([(task[0], task[1], i) for i, task in enumerate(tasks)], key = lambda x : x[0])
        n = len(tasks)
        result = []
        heap = []
        time = 0
        i = 0

        while i < n or heap:
            if not heap and i < n and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]

            while i < n and sorted_tasks[i][0] <= time:
                enqueue_time, processing_time, idx = sorted_tasks[i]
                heapq.heappush(heap, (processing_time, idx, enqueue_time))
                i += 1

            if heap:
                processing_time, idx, enqueue_time = heapq.heappop(heap)
                time += processing_time
                result.append(idx)

        return result