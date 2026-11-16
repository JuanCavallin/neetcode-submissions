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
            return result
        intervals.sort(key=lambda x: x.start)
        i = 0
        while i < len(intervals) - 1:
            while i < len(intervals) - 1 and intervals[i].end > intervals[i + 1].start:
                current += 1
                i += 1
                result = max(result, current)
            i += 1
            
        
        return result