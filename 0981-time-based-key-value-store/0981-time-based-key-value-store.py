from bisect import bisect, bisect_right

class TimeMap:

    def __init__(self):
        self.m = defaultdict(list) # key --> [(timestamp, value)]

 
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.m[key]
        if not arr:
            return ""
        idx = bisect_right(arr, timestamp, key=lambda x: x[0])
        if idx == 0:
            return ""
        return arr[idx - 1][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)