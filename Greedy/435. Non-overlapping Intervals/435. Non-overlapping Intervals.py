class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == []:
            return 0

        intervals.sort(key = lambda x : x[1])
        remove = 0
        end = intervals[0][1]
        for times in intervals[1:]:
            start = times[0]
            if start < end:
                remove += 1
            else:
                end = times[1]
        return remove
