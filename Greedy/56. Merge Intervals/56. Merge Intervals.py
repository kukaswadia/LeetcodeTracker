class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []

        intervals.sort(key = lambda x : x[0])
        result = [intervals[0]]
        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]
            last_end = result[-1][1]
            if start <= last_end:
                result[-1][1] = max(end, last_end)
            else:
                result.append(interval)
        return result 