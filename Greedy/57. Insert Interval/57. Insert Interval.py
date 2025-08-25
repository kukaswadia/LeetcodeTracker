# My solution 

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        inserted = False

        for interval in intervals:
            start = interval[0]
            end = interval[1]
            new_start = newInterval[0]
            new_end = newInterval[1]

            if end < new_start:
                result.append(interval)

            elif start > new_end:
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                result.append(interval)

            else:
                newInterval[0] = min(start, new_start)
                newInterval[1] = max(end, new_end)

        if not inserted:
            result.append(newInterval)

        return result
    

# Better solution that I didnt come up with 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        # Add all intervals that come before the newInterval
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge all overlapping intervals with the newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Add all intervals that come after the newInterval
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result