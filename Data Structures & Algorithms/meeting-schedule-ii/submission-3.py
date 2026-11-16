"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        result = 1
        current = 1
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        l, r = 0, 1

        while r < len(intervals) - 1:
            if intervals[l].end > intervals[r].start:
                current += 1
                result = max(result, current)
            else:
                l = r
                current = 1
            r += 1
            
        return result