class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.right) == 0 or num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        if len(self.right) > len(self.left) + 1:
            k = heapq.heappop(self.right)
            heapq.heappush(self.left, -k)
        if len(self.left) > len(self.right) + 1:
            k = heapq.heappop(self.left)
            heapq.heappush(self.right, -k)


    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0]) / 2
        if len(self.right) > len(self.left):
            return self.right[0]
        return -self.left[0]
        
        