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
        if not intervals:
            return result
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                result += 1
        
        return result