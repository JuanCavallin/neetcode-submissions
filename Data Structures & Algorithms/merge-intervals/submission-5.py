class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by 
        result = []

        intervals.sort(key=lambda x: x[1])
        result.append(intervals[0])
        
        for inter in intervals:
            if inter[0] <= result[-1][1]:
                result[-1][1] = inter[1]
            else:
                result.append(inter)

        return result