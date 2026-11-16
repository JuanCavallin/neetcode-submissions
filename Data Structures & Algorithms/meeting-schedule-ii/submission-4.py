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
            return 0
        rooms = 0
        starts = sorted(x.start for x in intervals)
        ends = sorted(x.end for x in intervals)

        start_ptr = 0
        end_ptr = 0

        while start_ptr < len(intervals) and end_ptr < len(intervals):
            if starts[start_ptr] < ends[end_ptr]:
                rooms += 1
                start_ptr += 1
            else:
                end_ptr += 1
                rooms -= 1
            result = max(result, rooms)
        
        return result