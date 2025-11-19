class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # sort meetings by start time 
        intervals.sort(key=lambda x : x[0])

        # min heap to track end times of ongoing meetings
        heap = []

        # add first meeting's end time
        heapq.heappush(heap, intervals[0][1])

        # process the remaining meetings
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # if current meeting is starting after the last meeting, resuse the room
            if start >= heap[0]:
                heapq.heappop(heap)
            
            # add current meeting's end time to the heap
            heapq.heappush(heap, end)

        return len(heap)